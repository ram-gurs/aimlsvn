# RAG quality regression test report

Run completed: 2026-10-12T17:18:29-04:00
Repository commit: `50c6978c9aa104c9e823958a6e9e82364f840ce1`

**21 passed, 213 warnings in 23.96s**

Tests: 21 · Failures: 0 · Errors: 0 · Skipped: 0

Command: `pytest tests/ -v --junitxml=/workspace/test-reports/rag-regression.xml`

## Results

| Test | Outcome | Seconds |
| --- | --- | ---: |
| tests.test_quality.test_pipeline_regression[fy2024_revenue] | PASSED | 6.791 |
| tests.test_quality.test_pipeline_regression[fy2024_eps] | PASSED | 4.145 |
| tests.test_quality.test_pipeline_regression[q3_quick_ratio] | PASSED | 7.329 |
| tests.test_utils.test_reject_incorrect_answer[changes0] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes1] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes2] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes3] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes4] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes5] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes6] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes7] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes8] | PASSED | 0.001 |
| tests.test_utils.test_reject_incorrect_answer[changes9] | PASSED | 0.001 |
| tests.test_utils.test_reject_unstructured_or_ambiguous_answer[Revenue was 600, not 612.4.] | PASSED | 0.001 |
| tests.test_utils.test_reject_unstructured_or_ambiguous_answer[{"metric": "revenue", "period": "FY2024", "unit": "USD_millions", "source": "10k_excerpt.txt", "value": 612.4} Revenue was actually 600.] | PASSED | 0.001 |
| tests.test_utils.test_reject_unstructured_or_ambiguous_answer[[{"metric": "revenue", "period": "FY2024", "unit": "USD_millions", "source": "10k_excerpt.txt", "value": 612.4}]] | PASSED | 0.001 |
| tests.test_utils.test_reject_unstructured_or_ambiguous_answer[{"metric": "revenue", "period": "FY2024", "unit": "USD_millions", "source": "10k_excerpt.txt", "value": 612.4, "value": 600}] | PASSED | 0.001 |
| tests.test_utils.test_accept_correct_answer[612.4_0] | PASSED | 0.001 |
| tests.test_utils.test_accept_correct_answer[612.4_1] | PASSED | 0.001 |
| tests.test_utils.test_accept_correct_answer[612.405] | PASSED | 0.001 |
| tests.test_utils.test_accept_json_fence | PASSED | 0.001 |

## Coverage and limitations

Three live Anthropic agent cases verify FY2024 revenue, FY2024 diluted EPS, and Q3-end quick ratio. Eighteen local assertion checks reject wrong values, signs, metrics, periods, units, source labels, duplicate fields, and ambiguous prose, and accept valid structured answers within tolerance.

Source labels are validated; actual citation provenance is not verified. Live model responses can vary between runs.

## Warnings

Dependency deprecations remain in LlamaIndex workflow inspection of Pydantic fields and use of the deprecated workflow is_running property. Warnings were not suppressed. See the log for counts and details.

## Artifacts

- [JUnit XML](rag-regression.xml)
- [Full pytest log](rag-regression.log)
