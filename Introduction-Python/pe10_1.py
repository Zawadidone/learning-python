
prijs = 4356

try:
    personen = int(input("Met hoeveel personen ga je reizen: "))

    som = prijs / personen

    if som < 0:
        raise AssertionError

    print(som)

except ZeroDivisionError:
    print("Delen door 0 kan niet!")
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except AssertionError:
    print("Negatieve getallen zijn niet toegestaan")
else:
    print("Onjuiste invoer")
