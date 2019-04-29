#!/usr/bin/python
import MySQLdb
import dis
import importlib

try:
    # Connect
    db = MySQLdb.connect(host="db4free.net",
                     user="elwseg",
                     passwd="Scarred_92",
                     db="iukmanagement")

    cursor = db.cursor()


    # Execute SQL select statement
    cursor.execute("SELECT * FROM Fahrzeug")

    # Get the number of rows in the resultset
    numrows = cursor.rowcount

    # Get and display one row at a time
    for x in range(0, numrows):
        row = cursor.fetchone()
        print ("Fahrzeugtyp:", row[0], "Funkrufnummer:", row[1], "Besatzung:", row[2], "Status:", row[3], "Organisation:", row[4])

except BaseException as ex:
    print('Fehler bei der Verbindung zur Datenbank. Überprüfen sie Link, Benutzer, Passwort und ausgewählte Datenbank', ex)
finally:
    # Close the connection
    db.close()
