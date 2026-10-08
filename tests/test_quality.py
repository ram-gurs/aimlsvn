import json
import pytest
from pathlib import Path
from pipeline import agent  # Adjust to your entry point function
from tests.test_utils import assert_numeric_match
import json
import pytest
from pathlib import Path

# Import the actual runner function from pipeline.py
from pipeline import run_step_6_agent  
from tests.test_utils import assert_numeric_match

def load_test_cases():
    data_path = Path(__file__).parent / "test_data" / "ground_truth_q3.json"
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.mark.parametrize("test_case", load_test_cases())
def test_pipeline_regression(test_case):
    # Execute query using the agent pipeline step
    result = run_step_6_agent(test_case["question"])
    
    # Extract string output (handles both dict and string returns)
    if isinstance(result, dict):
        answer_text = str(result.get("answer", result.get("response", "")))
    else:
        answer_text = str(result)
    
    # Assert numerical correctness
    assert assert_numeric_match(
        answer_text, 
        test_case["expected_value"], 
        test_case["tolerance"]
    ), f"Failed {test_case['id']}: expected {test_case['expected_value']}, got '{answer_text}'"