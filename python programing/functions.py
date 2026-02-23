#Functions is a block of code that performs a specific task
# def function name
def printdata(name):
    print("Hello: ",name)
printdata("Nishchal")

def sq(num):
    result = num * num
    return result
print(sq(5))

def func_pass():
    pass
func_pass()

def calc(a,b):
    return a + b, a - b, a * b
add, sub, mul = calc(10,5)
print(add)
print(sub)
print(mul)

def even(limit):
    for i in range(2, limit + 1, 2):
        print(i)
even(10)

def even(limit):
    if limit % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even(15))