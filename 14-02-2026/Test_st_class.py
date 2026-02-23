# used inside the class
# it will run for every class definition 0nce  it will run starting and  at ending of the class

class Testclass:

    def setup_class(cls):
        print("\nAPI authorization needed with username and password")
    def teardown_class(cls):
        print("\nAPI authorisation closed")

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