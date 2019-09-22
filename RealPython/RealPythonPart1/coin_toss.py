from random import randint

trails = 10000
flips = 0

for i in range(0, trails):
    flips += 1
    if randint(0, 1) == 0:
        while randint(0, 1) == 0:
            flips += 1
        flips += 1
    else:
        while randint(0, 1) == 1:
            flips += 1
        flips += 1

print(flips / trails)