
def convert(celsius):
    return (celsius * 1.80) + 32


def table():
    print("F\t\t\t C")
    for i in range(-30, 50, 10):
       print(f"{convert(i)} \t\t {i}")

table()
