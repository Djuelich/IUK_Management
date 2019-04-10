#!/usr/bin/python
import MySQLdb
import dis

# Connect
db = MySQLdb.connect(host="db4free.net",
                     user="elwseg",
                     passwd="Scarred_92",
                     db="iukmanagement")

cursor = db.cursor()

# Execute SQL select statement
cursor.execute("SELECT * FROM Fahrzeug")

# Commit your changes if writing
# In this case, we are only reading data
# db.commit()

# Get the number of rows in the resultset
numrows = cursor.rowcount

# Get and display one row at a time
for x in range(0, numrows):
   row = cursor.fetchone()
   print ("Fahrzeugtyp:", row[0], "Funkrufnummer:", row[1], "Besatzung:", row[2], "Status:", row[3], "Organisation:", row[4])
  


# Close the connection
db.close()
