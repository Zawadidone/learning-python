from sys import getrefcount as grc


print(grc(40))

a = 40
b = a
c = [b]

print(grc(40))


