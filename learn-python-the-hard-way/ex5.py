my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_height_cm = int(my_height * 2.54)
my_weight = 180
my_weight_kg = int(my_weight * 0.45)
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height_cm} centimeters tall.")
print(f"He's {my_weight_kg} kilo heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")
