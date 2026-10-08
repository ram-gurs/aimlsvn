import re

def assert_numeric_match(llm_output: str, expected_val: float, tolerance: float) -> bool:
    """Extracts numbers from LLM response and verifies match within tolerance."""
    found_numbers = re.findall(r"[-+]?\d*\.\d+|\d+", llm_output.replace(",", ""))
    found_floats = [float(num) for num in found_numbers]
    
    for num in found_floats:
        if abs(num - expected_val) <= tolerance:
            return True
    return False