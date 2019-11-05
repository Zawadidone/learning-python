def lang_genoeg(lengte):
	if type(lengte) != int:
		return "Graag een integer in cm :)"
	elif int(lengte) >= 120:
		return "Je bent lang genoeg voor de attractie!"
	else:
		return "Sorry, je bent te klein!"

print(lang_genoeg(120))
