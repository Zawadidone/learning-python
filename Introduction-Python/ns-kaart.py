

def inlezen_beginstation(stations):
    while True:
        begin_station = input("Wat is je beginstation?\n>> ")

        if begin_station in stations:
            return begin_station
        else:
            print(f"Deze trein komt niet in {begin_station}")


def inlezen_eindstation(stations, beginstation):
    while True:
        eind_station = input("Wat is je eindstation?\n>> ")

        if eind_station in stations:
            if stations.index(eind_station) > stations.index(beginstation):
                return eind_station
            else:
                print("De index is te laag")
        else:
            print(f"Deze trein komt niet in {eind_station}")


def omroepen_reis(stations, beginstation, eindstation):

    beginstation_index = stations.index(beginstation)
    eindstation_index = stations.index(eindstation)
    haltes = eindstation_index - beginstation_index
    print(f"""
Het beginstation {beginstation} is het {beginstation_index + 1}e station in het traject.
Het eindstation {eindstation} is het {eindstation_index + 1}e station in het traject.
De afstand bedraagt {haltes} stations(s).
De prijs van het kaartje is: {haltes * 5} euro
    """)

    for station in stations[beginstation_index:eindstation_index+1]:
        if station == beginstation:
            print(f"Jij stapt in de trein in: {station}")
        elif station == eindstation:
            print(f"Jij stapt uit in: {eindstation}")
        else:
            print(f"\t- {station}")


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
            'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch',
            'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
