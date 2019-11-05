
invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

getallen = list(map(int, invoer.split("-")))

print(f"Gesorteerde lijst van ints: {sorted(getallen)}")
print(f"Grootste getal: {max(getallen)} en kleinste getal: {min(getallen)}")
print(f"Aantal getallen: {len(getallen)} en som van de getallen {sum(getallen)}")
print(f"Gemiddeld {sum(getallen) / len(getallen)}")
