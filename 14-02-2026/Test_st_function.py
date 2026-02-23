

import pytest

def setup_function(function):
    print("Opening the browseer")

def teardoen_function(function):
    print("CLosing the browser")

def test_case1():
    print("Testcase1 is executed")

#testcase2
@pytest.mark.sanity
def test_case2():
    print("Testcase1 is executed")

@pytest.mark.regression
def test_case3():
    print("Testcase3 is executed")

def openbrowser():
    print("Browser opened")