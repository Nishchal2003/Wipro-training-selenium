#Sorting using lambda
numbers = [(1, 3), (2,4), (5,2), (4, 0)]

sort_number = sorted(numbers, key = lambda x : x[1])
print(sort_number)

#Extract
from datetime import datetime

date = datetime.now()

extract = lambda d  : (d.year,d.month,d.day, d.time())
print(extract(date))

dict1 = {1 : "Nishchal", 2 : "Nikhil"}
dict2 = {3 : "Kushal", 4 : "Suhas"}

empty_dict = {}
empty_dict.update(dict1)
empty_dict.update(dict2)
print(empty_dict)