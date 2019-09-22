import random

capitals_dict = {
        'Alabama':	'Montgomery',
        'Alaska':	'Juneau',
        'Arizona':	'Phoenix',
        'Arkansas':	'Little	Rock',
        'California':	'Sacramento',
        'Colorado':	'Denver',
        'Connecticut':	'Hartford',
        'Delaware':	'Dover',
        'Florida':	'Tallahassee',
        'Georgia':	'Atlanta'
}


def capital_city(capitals, city):
    while True:
        guess = input(f"What is the capital city of {capitals}?\n").lower()
        if guess == "exit":
            print(f"The answer was {city} \nGoodbye")
            break
        elif guess == city:
            print("Correct")
            break

state = random.choice(list(capitals_dict.keys()))
capital = capitals_dict[state]
capital_city(state, capital)
