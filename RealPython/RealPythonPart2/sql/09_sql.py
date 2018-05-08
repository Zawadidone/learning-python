import MySQLdb as db

# create connection
conn = db.connect("localhost", "root", "asdf", "projecten")

# create cursor
c = conn.cursor()

# create a dictionary of sql queries
sql = {'average': "SELECT avg(population) FROM projecten.population",
       'maximum': "SELECT max(population) FROM projecten.population",
       'minimum': "SELECT min(population) FROM projecten.population",
       'sum': "SELECT sum(population) FROM projecten.population",
       'count': "SELECT count(city) FROM projecten.population"}

# run each sql query item in the dictionary
for keys, values in sql.items():
       # run sql
       c.execute(values)

       # fetchone() retrieves one record from the query
       result = c.fetchone()

       # print keys with result
       print(f"{keys} : {result[0]}")

# close connection
conn.close()
