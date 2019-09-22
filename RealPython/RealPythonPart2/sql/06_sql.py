import MySQLdb as db

# create connection
conn = db.connect("localhost", "root", "asdf", "projecten")

# create cursor
c = conn.cursor()

# insert multiple records using a tuple
cities = [
                 ('Boston', 'MA', 600000),
                 ('Los Angeles', 'CA', 38000000),
                 ('Houston', 'TX', 2100000),
                 ('Philadelphia', 'PA', 1500000),
                 ('San Antonio', 'TX', 1400000),
                 ('San Diego', 'CA', 130000),
                 ('Dallas', 'TX', 1200000),
                 ('San Jose', 'CA', 900000),
                 ('Jacksonville', 'FL', 800000),
                 ('Indianapolis', 'IN', 800000),
                 ('Austin', 'TX', 800000),
                 ('Detroit', 'MI', 700000)
             ]
# sql statement
sql = "INSERT INTO projecten.population(city, state, population) VALUES(%s, %s, %s)"

# insert sql with list cities
c.executemany(sql, cities)

conn.commit()
# close connection
conn.close()
