number = int(input("Enter a positive integer: "))
for i in range(1, number + 1):
    divide = number % i
    if divide == 0:
        print(f"{i} is a divisor of {number}")
