
kluis = "kluis.txt"


def toon_aantal_kluizen():
    file = open(kluis, "r")
    regels = len(file.readlines())
    file.close()
    if regels >= 12:
        return "Er zijn geen kluizen beschikbaar"
    else:
        return 12 - regels


def nieuwe_kluis():
    kluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    file = open(kluis, "r")
    regels = len(file.readlines())
    file.close()
    file = open(kluis, "r")
    kluis_lijst = file.read().splitlines()
    file.close()
    if regels >= 12:
        return "Er zijn geen kluizen beschikbaar"
    else:
        for nummer in kluis_lijst:
            num = int(nummer.split(";")[0])
            kluizen.remove(num)
        pincode = int(input("Voer een pincode in: "))
        file = open(kluis, "a")
        file.write(f"{kluizen[0]};{pincode}")
        file.close()
        print(f"Kluisnummer {kluizen[0]} is ingesteld")


def kluis_openen():
    kluisnummer = int(input("Voer het kluisnummer in: "))
    kluiscode = int(input("Voor de kluiscode in: "))

    file = open(kluis, "r")
    kluis_lijst = file.read().splitlines()
    file.close()

    for k in kluis_lijst:
        if int(k.split(";")[0]) == kluisnummer:
            if int(k.split(";")[1]) == kluiscode:
                return "De kluis is open"
            else:
                return "De kluiscode klopt niet"
    return "De kluis bestaat niet!"


while True:
    keuze = int(input("""
1: Ik wil weten hoeveel kluizen nog vrij zijn 
2: Ik wil een nieuwe kluis 
3: Ik wil even iets uit mijn kluis halen 
>>> """))

    if keuze == 1:
        print(toon_aantal_kluizen())
    elif keuze == 2:
        print(nieuwe_kluis())
    elif keuze == 3:
        print(kluis_openen())
