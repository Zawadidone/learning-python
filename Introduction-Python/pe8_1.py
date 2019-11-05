
getallen = []
lengte = 0
som = 0

while True:
    try:
        getal = int(input("Geef een getal: "))

        if getal == 0:
            print(f"Er zijn {lengte} getallen ingevoerd, de som is: {som}")
            break
        else:
            getallen.append(getal)
            lengte = len(getallen)
            som = sum(getallen)

    except ValueError:
        print("Voer een getal in!")
