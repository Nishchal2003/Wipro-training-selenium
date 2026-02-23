# unit testing is type of testing done by the developers
# what component they have developed they do the testing for it before integrating it to the other modules
# get defects earlier
# Pytest in python , junit and nunit - java
# pytest is used ny developers and testers

# Test discovery - rules used to create the pytest tests
#-v -verbose- show detailed output

import pytest

#testcase`1`
def test_case1():
    print("Testcase1 is executed")

#testcase2
def test_case2():
    print("Testcase1 is executed")

def test_case3():
    print("Testcase3 is executed")

def openbrowser():
    print("Browser opened")