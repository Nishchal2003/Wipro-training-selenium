#2.write a test that runs only on Linux and skips on Windows.

import pytest
import sys

def test_case1():
    print("Test case1 completed")

@pytest.mark.skipif(sys.platform.startswith("win"),reason="Runs only on linux")
def test_case2():
    print("Test case2 is completed")

def test_case3():
    print("TEst case3 is completed")