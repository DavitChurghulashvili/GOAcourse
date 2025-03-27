numbers = []
for x in range(10):
    number = int(input("enter number: "))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
