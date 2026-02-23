def make_pretty(func):
    def inner():
        print("I am got decorated")
        func()
    return inner

@make_pretty
def Venilla():
    print("I am venilla")

@make_pretty
def Mango():
    print("I am Mango")

Venilla()
Mango()