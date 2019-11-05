from datetime import datetime

while True:
    with open("hardlopers.txt", "a") as file:
        name = input("Registreer een hardloper: ")

        time = datetime.today()
        time_digital = time.strftime("%H:%M:%S")
        time_agenda = time.strftime("%a %d %b %Y")

        file.write(f"{time_agenda}, {time_digital}, {name}\n")
