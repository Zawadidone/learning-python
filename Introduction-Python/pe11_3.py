from json import load, dump

gegevens = []

with open("inloggers.json", "r+") as f:

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == "einde":
            dump(gegevens, f)
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        gegevens.append({
            "naam": naam,
            "voorletters": voorl,
            "geb_datum": gbdatum,
            "e-mail": email
        })




