from random import randint


def monopolyworp():
    count = 0

    while True:
        dobbel = randint(1, 6), randint(1, 6)

        count += 1

        if count == 3:
            if dobbel[0] == dobbel[1]:
                print(f"{dobbel[0]} + {dobbel[1]} = {dobbel[0] + dobbel[1]} (dubbel)")
            else:
                print(f"{dobbel[0]} + {dobbel[1]} = (direct naar gevangenis)")
            break
        elif dobbel[0] == dobbel[1]:
            print(f"{dobbel[0]} + {dobbel[1]} = {dobbel[0] + dobbel[1]} (dubbel)")
        else:
            print(f"{dobbel[0]} + {dobbel[1]} = {dobbel[0] + dobbel[1]}")


monopolyworp()
