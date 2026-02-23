#5.You have 5 parameterized cases.2 are known bugs.Mark only those 2 cases as xfail without marking entire test.

import pytest

@pytest.mark.parametrize("a,b,result",[
    (1, 2, 3),
    (2, 3, 5),
    (4, 5, 9),
    pytest.param(10, 2, 11,marks=pytest.mark.xfail(reason="Known bug")),
    pytest.param(12, 2, 11,marks=pytest.mark.xfail(reason="Known bug"))
    ]
)
def test_add(a, b, result):
    assert a + b == result