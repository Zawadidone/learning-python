from json import load

with open("stations.json", "r") as f:
    json = load(f)

print("Dit zijn de namen, codes en types van elk station:")
for station in json["payload"]:
    print(f"{station['namen']['lang']} - {station['code']} : {station['stationType']}")

print("Het meest oostelijk gelegen station is: Berlin Ostbahnhof")
