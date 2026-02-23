#1.Write a test that is skipped because a feature is not implemented yet.

import pytest

def test_case1():
    print("Test case1 completed")

@pytest.mark.skip(reason="Feature not implemented yet")
def test_case2():
    print("Test case2 is completed")

def test_case3():
    print("TEst case3 is completed")