def celsius(c):
    f = c * 9 / 5 + 32
    return f


def fahrenheit(f):
    c = (f - 32) * 5 / 9
    return c

cel = int(input("Give a celsius: "))
print(celsius(cel))
fahr = int(input("Give a fahrenheit "))
print(fahrenheit(fahr))
