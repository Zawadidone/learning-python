with open("poem.txt", "r") as file:
    for l in file.readlines():
        print(l)


poem_in = open("poem.txt", "r")
poem_out = open("output.txt", "w")

for l in poem_in.readlines():
    poem_out.write(l)

poem_in.close()
poem_out.close()

poem = open("output.txt", "a")
poem.write("\nhoi")
poem.close()