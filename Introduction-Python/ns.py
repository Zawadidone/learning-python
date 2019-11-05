
def standaardtarief(afstandKM):
	"""
	De functie rekent het tarief per KM uit.
	:param (float) afstandKM: De afstand in KM
	:return: (float) Standaard tarief voor het aantal kilometers
	"""
	if type(afstandKM) != int:
		print("Graag een decimaal getal")
		return 0.00
	elif afstandKM <= 0:
		return 0.00
	elif afstandKM > 50:
		return 15 + (0.60 * afstandKM)
	else:
		return 0.80 * afstandKM


def ritprijs(leeftijd, weekendrit, afstandKM):
	"""
	De functie reken de ritpijs uit afhankelijk van leeftijd en weekendrit
	:param (int) leeftijd: De leeftijd van de treinreiziger
	:param (bool) weekendrit: Wel of geen weekendrit
	:param (float) afstandKM: De afstand in KM
	:return: (float) Rit prijs
	"""
	standaard_tarief = standaardtarief(afstandKM)

	if leeftijd < 12 or leeftijd >= 65:
		if weekendrit:
			ritprijs = standaard_tarief * 0.65
		else:
			ritprijs = standaard_tarief * 0.70
	else:
		if weekendrit:
			ritprijs = standaard_tarief * 0.60
		else:
			ritprijs = standaard_tarief
	return float("%.2f" % ritprijs)


print(ritprijs(11, False, 10))
print(ritprijs(11, True, 10))
print(ritprijs(12, False, 10))
print(ritprijs(12, True, 10))
print(ritprijs(64, True, 10))
print(ritprijs(64, False, 10))
print(ritprijs(65, True, 10))
print(ritprijs(65, False, 10))
