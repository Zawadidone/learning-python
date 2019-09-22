desserts = ["ice cream", "cookies"]
desserts.sort()
print(desserts.index("ice cream"))
food = desserts[:]
food.extend(["broccoli", "turnips"])
print(f"{desserts} \n{food}")
food.remove("cookies")
print(food[0:2])
cookies = "cookies, cookies, cookies"
breakfast = cookies.split(", ")
print(breakfast)


def take_number(numbers):
    for i in numbers:
        if 1 > i and i < 20:
            print(i)

list_numbers = [2, 4, 8, 16, 32, 64]
take_number(list_numbers)
