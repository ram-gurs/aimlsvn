import json
import math
import re

import pytest


def assert_numeric_match(value, expected_val, tolerance):
    """Compare one numeric value rather than extract numbers from prose."""
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        return False
    if isinstance(value, str) and not re.fullmatch(r"[-+]?\d+(?:\.\d+)?", value):
        return False
    number = float(value)
    return math.isfinite(number) and abs(number - expected_val) <= tolerance


def assert_answer_match(output, case):
    """Validate a single answer and its financial context."""
    text = output.strip()
    fence = re.fullmatch(r"```(?:json)?\s*\n(.*?)\n```", text, re.DOTALL)
    if fence:
        text = fence.group(1)

    def unique_fields(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate answer field")
            result[key] = value
        return result

    try:
        answer = json.loads(text, object_pairs_hook=unique_fields)
    except (ValueError, TypeError):
        return False
    if not isinstance(answer, dict) or set(answer) != {
        "metric", "period", "unit", "value", "source"
    }:
        return False
    for field in ("metric", "period", "unit"):
        if answer[field] != case[field]:
            return False
    if answer["source"] != case["expected_document"]:
        return False
    return assert_numeric_match(answer["value"], case["expected_value"], case["tolerance"])


CASE = {
    "metric": "revenue", "period": "FY2024", "unit": "USD_millions",
    "expected_document": "10k_excerpt.txt", "expected_value": 612.4, "tolerance": 0.01,
}
ANSWER = {
    "metric": "revenue", "period": "FY2024", "unit": "USD_millions",
    "source": "10k_excerpt.txt", "value": 612.4,
}


@pytest.mark.parametrize("changes", [
    {"value": 600}, {"value": -612.4}, {"value": True}, {"value": float("nan")},
    {"value": "Not 612.4; actually 600"}, {"metric": "cash"}, {"period": "Q3"},
    {"unit": "USD"}, {"source": "q3_earnings_call.txt"}, {"extra": "612.4"},
])
def test_reject_incorrect_answer(changes):
    assert not assert_answer_match(json.dumps(ANSWER | changes), CASE)


@pytest.mark.parametrize("output", [
    "Revenue was 600, not 612.4.",
    json.dumps(ANSWER) + " Revenue was actually 600.",
    '[' + json.dumps(ANSWER) + ']',
    json.dumps(ANSWER)[:-1] + ', "value": 600}',
])
def test_reject_unstructured_or_ambiguous_answer(output):
    assert not assert_answer_match(output, CASE)


@pytest.mark.parametrize("value", [612.4, "612.4", 612.405])
def test_accept_correct_answer(value):
    assert assert_answer_match(json.dumps(ANSWER | {"value": value}), CASE)


def test_accept_json_fence():
    assert assert_answer_match('```json\n' + json.dumps(ANSWER) + '\n```', CASE)
