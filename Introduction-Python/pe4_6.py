s = "Guido van Rossum heeft programmeertaal Python bedacht."

for l in s:
    if l in ['a', 'e', 'i', 'o', 'u']:
        print(l, end=' ')
