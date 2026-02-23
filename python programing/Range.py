a = range(5)
print(a[1])
print(a[3])

for attempt in range(3):
    pin = input("Enter the pin: ")
    if(pin == 1234):
        print("Acess granted")
        break
    else:
        print("Try again")

prices = [100, 200, 300, 400]

for i in range(len(prices)):
    if i % 2 == 0:
        print("Discount apllied onitem{1}")

import time

for second in range(10):
    print("Checking")
    time.sleep(1)