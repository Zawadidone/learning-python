
bruin = {"Boxtel", "Best", "Breukenlaan", "Eindhoven", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}

groen = {"Boxtel", "Best", "Breukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"}

print("De volgende stations zitten in beide trajecten:")
print(bruin.intersection(groen), "\n")


print("De volgende stations staan alleen op traject bruin:")
print(bruin.difference(groen), "\n")


print("Dit zijn alle stations van beide trajecten")
print(bruin.union(groen), "\n")

