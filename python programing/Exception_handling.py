
import json
try:
    with open(r"C:\Users\Nikhil\PycharmProjects\PythonProject\Data formats\employee.json", "r") as file:
        data = json.load(file)
    print(data)

except FileNotFoundError:
    print("Error : File not found")


try:
    digit = int(input("Enter a digits"))
    print(digit)

except Exception as e:
    print("Not a valid input")

try:
     a = int(input("Enter the number"))
     b = int(input("Enter the number"))
     print(a // b)
except ZeroDivisionError :
    print("Cannot divide by zero")

import random
import string

random_char = random.choice(string.ascii_letters)
print("Random alphabetical character:", random_char)

length = random.choice(range(5, 11))
random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
print("Random alphabetical string:", random_string)

fixed_length = 8
fixed_string = ''.join(random.choice(string.ascii_letters) for _ in range(fixed_length))
print("Fixed length alphabetical string:", fixed_string)


