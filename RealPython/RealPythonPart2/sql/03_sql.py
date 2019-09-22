import MySQLdb

# start connection
db = MySQLdb.connect("localhost", "root", "asdf", "projecten")

# create cursor
c = db.cursor()

# insert multiple records using a tuple
cities = [
    ('Boston', 'MA', 600000),
    ('Chicago', 'IL', 2700000),
    ('Houston', 'TX', 2100000),
    ('Phoenix', 'AZ', 1500000)
]


# insert data into table with list cities
c.executemany("INSERT INTO projecten.population(city, state, population) VALUES(%s, %s, %s)", cities)

# commit changes
db.commit()

# close connection
db.close()
