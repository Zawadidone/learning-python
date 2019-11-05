
namen = {}

while True:
    naam = input("Volgende naam: ")

    if naam:
        if naam in namen:
            namen[naam] += 1
        else:
            namen[naam] = 1
    else:
        for key, value in namen.items():
            if value == 1:
                print(f"Er is {value} student met de naam {key}")
            else:
                print(f"Er zijn {value} studenten met de naam {key}")
        if not namen:
            print("Er zijn geen namen ingevuld")
        break
