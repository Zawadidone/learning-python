
def kwadraten_som(grondgetallen):
	som = 0
	for g in grondgetallen:
		if g > 0:
			som += g ** 2
	return som


print(kwadraten_som([4, 5, 3, -81]))
