
while True:
    try:
        uurloon = int(input("Wat verdien je per uur: "))

        uur_aantal = int(input("Hoeveel uur heb je gewerkt: "))

        print(f"{uur_aantal} uur werken levert {uur_aantal * uurloon} euro op")
        break
    except ValueError:
        print("Voer een getal in!")
