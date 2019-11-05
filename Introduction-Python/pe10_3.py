
while True:
    try:
        file = input("In welk bestand staan de kaartnummers: ")
        count_lines = len(open(file, "r").readlines())
        file_lines = open(file, "r").read().splitlines()

        kaartnummers = []
        for l in file_lines:
            line = l.split(",")
            kaartnummers.append(int(line[0]))
        max_kaartnummer = max(kaartnummers)
        print(f"Deze file telt {count_lines} regels\nHet grootste kaartnummer is: {max_kaartnummer} en staat op regel {kaartnummers.index(max_kaartnummer) + 1}")
        break
    except FileNotFoundError:
        print("Het bestand bestaat niet!")
