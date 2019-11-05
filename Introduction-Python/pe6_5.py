

def gemiddelde():
    zin = input("Vul een zin in: ")

    zin_len = zin.split(" ")
    gem = sum(len(str(i)) for i in zin_len) / len(zin_len)
    print(gem)

gemiddelde()
