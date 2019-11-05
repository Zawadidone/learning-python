cijferICOR = 7
cijferPROG = 9
cijferCSN = 8

gemiddelde = sum([cijferICOR, cijferPROG, cijferCSN]) / 3

beloning = sum([cijferICOR, cijferPROG, cijferCSN]) * 30

overzicht = f"""Mijn cijfers (gemiddeld een {gemiddelde}) leveren een beloning van €{beloning} op!"""

print(overzicht)
