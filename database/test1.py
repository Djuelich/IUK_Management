#!/usr/bin/python
import MySQLdb
import dis
import importlib

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QMessageBox, QListWidget
from PyQt5.QtCore import QSize

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



class MyWindow(QMainWindow):
    def __init__(self):
        global txts

        #Konstruktor von QMainwindow aufrufen
        super().__init__()

        #Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(800, 600))
        self.setWindowTitle('IUK Management')        

        #GridLayout für Widget in Main-Window (Layout von Main-Window kann nicht verändert werden)

#Fenster öffnen; das Programm läuft, bis das Fenster geschlossen wird
app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
