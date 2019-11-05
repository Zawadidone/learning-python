

def seizoen(maand):
    if maand in [12, 1, 2]:
        return "Winter"
    elif maand in [3, 4, 5]:
        return "Lente"
    elif maand in [6, 7, 8]:
        return "Zomer"
    elif maand in [9, 10, 11]:
        return "Herfst"
    else:
        return "Geef een getal tussen 0 en 12"

print(seizoen(1))

