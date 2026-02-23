import pytest


def test_case1():
    print("Testcase1 is executed")

#testcase2
@pytest.mark.regression
def test_case2():
    print("Testcase2 is executed")

@pytest.mark.sanity
def test_case3():
    print("Testcase3 is executed")

def openbrowser():
    print("Browser opened")