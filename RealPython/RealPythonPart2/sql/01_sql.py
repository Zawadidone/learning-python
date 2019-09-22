# import MySQLdb to connect to database with python3.6
import MySQLdb

# open database connection
db = MySQLdb.connect("localhost", "root", "asdf", "projecten")

# prepare a cursor object using cursor() method
c = db.cursor()

c.execute("CREATE TABLE population(city TEXT, state TEXT, population INT)")

db.close()

