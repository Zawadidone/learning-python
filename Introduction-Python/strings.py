
# count characters
print("Supercalifragilisticexpialidocious \nLength:", len("Supercalifragilisticexpialidocious"))

# if ice in string
var = "Supercalifragilisticexpialidocious"
if "ice" in var:
    print(f"ice exists in string: {var}")
else:
    print(f"ice doesn't exist in string: {var}")

# compare length of 2 strings
var_one = "Antidisestablishmentarianism"
var_two = "Honorificabilitudinitatibus"

if len(var_one) > len(var_two):
    print(f"{var_one} is longer than {var_two}")
else:
    print(f"{var_one} is smaller than {var_two}")

# print items in alphabetical order
componisten = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']

print(sorted(componisten))
