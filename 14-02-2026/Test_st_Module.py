# module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection
# setup_module - -> only one per file
# setup_class() → one per class
# setup_method() → one per class
# setup_function() → one per class

import  pytest

def setup_module(module):
    print("\nOpen the db connection")

def teardown_module(module):
    print("\nClosing the db connection")

def test_read():
    print("Reading the db")

def test_write():
    print("Writing into the db")

def test_update():
    print("Updating the db")
