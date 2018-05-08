# import the MySQLdb library
import MySQLdb

# create the connection object
db = MySQLdb.connect("localhost", "root", "asdf", "projecten")

# prepare a cursor object using cursor() method
c = db.cursor()

# execute statements "
c.execute("INSERT INTO projecten.population VALUES('New York City', 'NY', 8200000)")
c.execute("INSERT INTO projecten.population VALUES('San Francisco', 'CA', 800000)")

db.commit()

db.close()
