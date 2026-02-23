numbers = [1,2,3,4,5,6]

print(max(numbers))
for num in numbers[:]:
    if num % 2 != 0:
        numbers.remove(num)

print(numbers)

result = 1
for num in numbers:
    result = result * num

print(result)