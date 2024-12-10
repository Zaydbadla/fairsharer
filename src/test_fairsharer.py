import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fair_sharer import fair_sharer

def test_fair_sharer():

    test_cases = [
        {"input": ([0, 1000, 800, 0], 1), "expected": [100, 800, 900, 0]},
        {"input": ([0, 1000, 800, 0], 2), "expected": [100, 890, 720, 90]},
        {"input": ([50, 0, 0, 50], 1, 0.5), "expected": [25, 25, 25, 25]},
    ]

    for case in test_cases:
        result = fair_sharer(*case["input"])
        assert result == case["expected"], f"Expected {case['expected']} but got {result}"
