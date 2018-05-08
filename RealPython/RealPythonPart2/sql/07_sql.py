# import MySQLdb to connect to database with python3.6
import MySQLdb as db

# open database connection
conn = db.connect("localhost", "root", "asdf", "projecten")

# prepare a cursor object using cursor() method
c = conn.cursor()

# c.execute("CREATE TABLE regions(city TEXT, region TEXT)")

cities = [
             ('New York City', 'Northeast'),
             ('San Francisco', 'West'),
             ('Chicago', 'Midwest'),
             ('Houston', 'South'),
             ('Phoenix', 'West'),
             ('Boston', 'Northeast'),
             ('Los Angeles', 'West'),
             ('Houston', 'other'),
             ('Philadelphia', 'Northeast'),
             ('San Antonio', 'South'),
             ('San Diego', 'West'),
             ('Dallas', 'South'),
             ('San Jose', 'West'),
             ('Jacksonville', 'South'),
             ('Indianapolis', 'Midwest'),
             ('Austin', 'South'),
             ('Detroit', 'Midwest')
              ]

c.executemany("INSERT INTO projecten.regions(city, region) VALUES(%s, %s)", cities)

# c.execute("SELECT * FROM projecten.regions ORDER BY  region ASC")

# fetch all rows
rows = c.fetchall()

# print all rows in for loop
for r in rows:
    print(r[0], r[1])

# commit changes no way back
conn.commit()

# close connection
conn.close()
