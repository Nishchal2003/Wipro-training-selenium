# lambda function - anonymous(nameless) functions, one line , simple operations

# syntax lambda arguments: expressions


# it can have any number of arguments
# must have only one expression
# the expressions is automatically returned


# functions - function name, arguments , return type, code,


#normal function

def add(a , b):
    return a + b
print(add(3,2))

add = lambda a, b : a + b
print(add(3,2))

odd_even = lambda x : "Even" if  x%2 == 0 else "Odd"
print(odd_even(3))

numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

status = ['pass', 'fail', 'pass', 'fail']
failed = list(filter(lambda s : s == 'fail', status))
print(failed)

data = ["hello", "", "world", "","python"]

from functools import reduce

nums =[10, 20, 30, 40, 50]
print(reduce(lambda x, y : x + y, nums))
print(reduce(lambda x, y : x * y, nums))
print(reduce(lambda x, y: x if x > y else y, nums))
print(reduce(lambda x, y: x if x < y else y, nums))

# map - transform the data - the function is applied to every element

nums = [10, 20, 30, 40]
squares = list(map(lambda x: x + x, nums))
print(squares)

# Sorting lambda
data = [(1, 3), (4, 1), (2, 2)]
sorteddata = sorted(data, key = lambda  x : x)
print(sorteddata)
sorteddata = sorted(data, key = lambda  x : x[1])
print(sorteddata)

marks = {"A" : 75, "B" : 90, "C" : 60}
sortedmarks = dict(sorted(marks.items(), key = lambda x : x[1]))
print(sortedmarks)