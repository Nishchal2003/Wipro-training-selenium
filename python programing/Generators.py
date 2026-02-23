def numbrers():
    return [1, 2, 3, 4]
print(numbrers())

def Generators():
    print("Printing 1")
    yield 1
    print("Printing 2")
    yield 2
    print("Printing 3")
    yield 3
    print("Printing 4")
    yield 4

return_value = Generators()

print(next(return_value))
print(next(return_value))
print(next(return_value))