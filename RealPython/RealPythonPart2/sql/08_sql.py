import MySQLdb as db

# create connection
conn = db.connect("localhost", "root", "asdf", "projecten")

# create cursor
c = conn.cursor()

# execute statement
c.execute("""
SELECT DISTINCT population.city, population.population, regions.region 
FROM projecten.population, projecten.regions
WHERE population.city = regions.city
ORDER BY population.city ASC
""")

# fetch all rows
rows = c.fetchall()

# print all rows with a for loop
for r in rows:
    print("City:	" + r[0])
    print("Population:	" + str(r[1]))
    print("Region:	" + r[2])
    print("")

conn.commit()

conn.close()
