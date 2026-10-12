import json
from pathlib import Path

import pytest

from config import init_models
from data_loader import load_documents_and_build_indexes
from pipeline import run_step_6_agent
from tests.test_utils import assert_answer_match

def load_test_cases():
    data_path = Path(__file__).parent / "test_data" / "ground_truth_q3.json"
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def indexes():
    init_models()
    data_path = Path(__file__).resolve().parents[1] / "data"
    _, document_indexes = load_documents_and_build_indexes(data_dir=str(data_path))
    return document_indexes


@pytest.mark.asyncio
@pytest.mark.parametrize("test_case", load_test_cases(), ids=lambda case: case["id"])
async def test_pipeline_regression(test_case, indexes):
    # Execute query using the agent pipeline step
    query = test_case["question"] + (
        '\nReturn only one JSON object with exactly these fields: '
        '"metric", "period", "unit", "value", "source". '
        f'Use metric="{test_case["metric"]}", period="{test_case["period"]}", '
        f'unit="{test_case["unit"]}". '
        'The value must be the numeric answer supported by the documents, '
        'not a comparison, threshold, or prior-period value. '
        'Use the supporting input filename for source: 10k_excerpt.txt for '
        'the 10-K tool, q3_earnings_call.txt for the call tool, or '
        'internal_risk_policy.txt for the policy tool. '
        'If the answer is unavailable, use null for value. No extra fields or prose.'
    )
    result = await run_step_6_agent(indexes, query)
    
    # Extract string output (handles both dict and string returns)
    if isinstance(result, dict):
        answer_text = str(result.get("answer", result.get("response", "")))
    else:
        answer_text = str(result)
    
    assert assert_answer_match(answer_text, test_case), (
        f"Failed {test_case['id']}: expected {test_case}, got '{answer_text}'"
    )
