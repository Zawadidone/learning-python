leeftijd = int(input("Geef je leeftijd: "))

paspoort = str(input("Nederlands paspoort (ja/nee): "))

if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen")
else:
    print("Je mag niet stemmen!")
