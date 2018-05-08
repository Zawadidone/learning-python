import MySQLdb

# create connection
db = MySQLdb.connect("localhost", "root", "asdf", "projecten")

# create cursor
c = db.cursor()

cities = ["New York", "NY", 8400000]
try:
    # execute sql statement
    c.execute("INSERT INTO projecten.population(city, state, population) VALUES(%s, %s, %s)", cities)

    # commit changes
    db.commit()
except MySQLdb.Error as e:
    print(e)
finally:
    db.close()
