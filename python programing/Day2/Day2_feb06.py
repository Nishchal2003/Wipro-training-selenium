Student = {1 : "Nishchal", 2 : "Abhishek", 3 : "Rahul"}
print(Student)
print(Student[2])
#print(Student[5])
Student[2] = "Manjunath"
print(Student)
del Student[3]
print(Student)
Student.pop(2)
print(Student)
print(len(Student))
print(Student.keys())
print(Student.values())
print(Student.items())

from functools import reduce
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x : x % 2 == 0,nums))
print(evens)
sqaure = list(map(lambda x : x * x, nums))
print(sqaure)
sum = reduce(lambda x, y : x + y, nums)
print(sum)

salaries = [25000, 40000, 32000, 18000]

lists = list(filter(lambda x : x > 30000, salaries))
print(lists)
increment = list(map(lambda x : x * 0.1, lists))
print(increment)

