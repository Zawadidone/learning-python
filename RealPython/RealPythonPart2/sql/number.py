import MySQLdb as db
import random
# create connection
conn = db.connect("localhost", "root", "asdf", "projecten")

# create cursor
c = conn.cursor()

# if table exist from previous script drop table
c.execute("DROP TABLE IF EXISTS projecten.numbers")

# create new table
c.execute("CREATE TABLE numbers(number INT)")

# insert 100 random numbers
for i in range(100):
    number = random.randint(0, 100)
    c.execute("INSERT INTO projecten.numbers(number) VALUES(%s)", (number,))

# commit changes no way back
conn.commit()

prompt = """
    Select the operation that you want to perform [1-5]:
    1. Average
    2. Max
    3. Min
    4. Sum
    5. Exit
    """
while True:
    x = int(input(prompt))

    # if user enters 1-4
    if x in [1, 2, 3, 4]:
        # parse x into dictionary for operation
        operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[x]

        print(operation)

        # retrieve data
        c.execute(f"SELECT {operation}(number) FROM projecten.numbers")

        # fetch one row from query
        row = c.fetchone()

        # print result to screen
        print(f"{operation} : {row[0]}")
    elif x == 5:
        print("bye")

        break


