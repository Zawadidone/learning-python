
a = 6
b = 7
c = (a + b) / 2

# if 75 is bigger than a and smaller than b
if 75 > a and 75 < b:
	print(f"75 is bigger than {a} and smaller than {b}")
else:
	print(f"Nope")

voornaam = "Zawadi"
achternaam = "Done"
tussenvoegsel = "x"

mijnnaam = voornaam + " " + tussenvoegsel + " " + achternaam

if len(mijnnaam) == len(voornaam + achternaam + tussenvoegsel):
	print(f"the length of '{mijnnaam}' == {voornaam, achternaam, tussenvoegsel}")
else:
	print(f"the length of '{mijnnaam}' != {voornaam, achternaam, tussenvoegsel}")

if len(tussenvoegsel * 5) < len(mijnnaam):
	print(f"'{mijnnaam}' is bigger then 5 * {tussenvoegsel}")
else:
	print(f"'{mijnnaam}' is smaller than 5 * {tussenvoegsel}")

if tussenvoegsel in achternaam:
	print(f"'{tussenvoegsel}' exists in {achternaam}")
else:
	print(f"'{tussenvoegsel}' doesn't exist in {achternaam}")
