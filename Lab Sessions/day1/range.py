def in_range(num, start, end):
    return start <= num <= end

print(in_range(5, 1, 10))

#Even numbers
def print_even():
    for i in range(2, 51, 2):
        print(i)

print_even()

#Adding numbers
def sum_numbers():
    total = 0
    for i in range(1, 101):
        total += i
    return total

print(sum_numbers())

#Divisible by 5
for i in range(1, 101):
    if i % 5 == 0:
        print(i)

#square of numbers
for i in range(1, 11):
    print(i * i)

