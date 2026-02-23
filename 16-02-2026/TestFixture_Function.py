import pytest

@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("Enter the name")
    print("Enter the password")
    print("Click the login button")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("User loged out")

