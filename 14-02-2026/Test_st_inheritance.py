# Used in the class
# runs before and after the test methods inside the class
# In case of inheritance setup and teardown is not considered

class Testclass:

    def setup_class(cls):
        print("\nAPI authorization needed with username and password")

    def teardown_class(cls):
        print("\nAPI authorisation closed")

    def setup_method(method):
        print("Opening the browser")

    def teardown_method(method):
        print("Closing the browser")

    def test_case1(self):
        print("Testcase1 is executed")

    # testcase2
    def test_case2(self):
        print("Testcase1 is executed")

    def test_case3(self):
        print("Testcase3 is executed")

class Testclass2:
    def test_case1(self):
        print("Testcase1 is executed")

    # testcase2
    def test_case2(self):
        print("Testcase1 is executed")

    def test_case3(self):
        print("Testcase3 is executed")