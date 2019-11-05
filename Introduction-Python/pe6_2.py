
with open("kaartnummers.txt", "r") as file:
    lines = file.read().splitlines()
    for l in lines:
        line = l.split(",")
        print(f"{line[1]} heeft kaartnummer: {line[0]}")
