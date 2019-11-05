
count_lines = len(open("kaartnummers.txt", "r").readlines())
file_lines = open("kaartnummers.txt", "r").read().splitlines()

kaartnummers = []
for l in file_lines:
    line = l.split(",")
    kaartnummers.append(int(line[0]))
max_kaartnummer = max(kaartnummers)
print(f"Deze file telt {count_lines} regels\nHet grootste kaartnummer is: {max_kaartnummer} en staat op regel {kaartnummers.index(max_kaartnummer) + 1}")
