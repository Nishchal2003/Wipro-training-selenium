#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)

import pytest
@pytest.mark.xfail(reason = "Know bug in the third")
def test_function_with_bug():
    assert(1 + 1) == 3# This assertion will fail as excpected

    # testcase2
@pytest.mark.regression
def test_case2():
    print("Testcase2 is executed")

@pytest.mark.sanity
def test_case3():
    print("Testcase3 is executed")

@pytest.mark.db
def openbrowser():
    print("Browser opened")