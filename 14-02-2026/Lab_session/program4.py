#4.Mark a failing test as xfail with reason: "Bug #123".

import pytest

@pytest.mark.xfail(reason="Known bug")
def test_case1():
    assert 1 + 1 == 3

def test_case2():
    print("Test case2 is completed")