weight = 0.2
animal = "newt"
print(weight, "kg is the weight of the", animal)

weight = 0.2
animal = "newt"
print("{} kg is the weight of the {}".format(weight, animal))

weight = 0.2
animal = "newt"
print("{0} kg is the weight of the {1}".format(weight, animal))


print("{weight} kg is the weight of the {animal}".format(weight=0.2, animal="newt"))
