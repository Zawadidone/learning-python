import MySQLdb

# create connection
conn = MySQLdb.connect("localhost", "root", "asdf", "projecten")

# create cursor
c = conn.cursor()

# update data
c.execute("UPDATE projecten.population SET population = 9000000 WHERE city = 'New York'")

# select the hole table
c.execute("SELECT * FROM projecten.population")

# fetch all rows
rows = c.fetchall()

# print all rows in a for loop
for r in rows:
    print(r[0], r[1], r[2])

# close connection
conn.close()
