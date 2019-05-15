#!/usr/bin/python
import MySQLdb
import dis
import importlib

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QLabel,QPushButton
from PyQt5.QtCore import QSize, pyqtSlot, Qt, QTimer
from PyQt5.QtGui import QIcon


#Window and Table-section
class App(QWidget):

    def __init__(self):
        super().__init__()
        screen = app.primaryScreen()
        size = screen.size()
        self.title = 'IUK-Management'
        self.left = 0
        self.top = 0
        self.width = size.width()/2
        self.height = size.height()/2
        self.initUI()
        print("initUI-Init aufruf")
        self.setLayout(self.layout)
        print("setLayout aufruf") 
        print("init aufruf")

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()
        self.creatCounter()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.setAlignment(Qt.AlignCenter) 
        self.layout.addWidget(self.itemCounter1)
        self.layout.addWidget(self.itemCounter2)
        self.layout.addWidget(self.itemCounter3)
        self.layout.addWidget(self.itemCounter4)

        # Show widget
        self.show()
        print("initUI aufruf")


    #try to create a table with DBS-data
    def createTable(self):
        # Create table
        self.getVehicles()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(numrows+1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Fahrzeugtyp"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Funkrufnummer"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Besatzung"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Status"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Organisation"))
        """self.tableWidget.setItem(1,0, QTableWidgetItem(row[0]))
        self.tableWidget.setItem(1,1, QTableWidgetItem(row[1]))
        self.tableWidget.setItem(1,2, QTableWidgetItem(row[2]))
        self.tableWidget.setItem(1,3, QTableWidgetItem(row[3]))
        self.tableWidget.setItem(1,4, QTableWidgetItem(row[4]))"""
        self.tableWidget.move(0,0)
        for x in range(0, numrows):
            row = cursor.fetchone()
            line = x+1
            self.tableWidget.setItem(line,0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(line,1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(line,2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(line,3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(line,4, QTableWidgetItem(row[4]))
        print("createTable aufruf")

    def creatCounter(self):
        self.itemCounter1 = QLabel()
        self.itemCounter2 = QLabel()
        self.itemCounter3 = QLabel()
        self.itemCounter4 = QLabel()
        self.itemCounter1.setText("Anzahl Fahrzeuge: {}".format(numrows))
        self.itemCounter2.setText("Anzahl RTWs: {}".format(numrows2))
        self.itemCounter3.setText("Anzahl KTWs: {}".format(numrows3))
        self.itemCounter4.setText("Anzahl NEFs: {}".format(numrows4))
        print("createCounter aufruf")

    def databaseConnection(self):
        global db
        #Database-connection-section
        try:
            # Connect
            db = MySQLdb.connect(host="db4free.net",    
                                user="elwseg",
                                passwd="Scarred_92",
                                db="iukmanagement")

        except BaseException as ex:
            print('Fehler bei der Verbindung zur Datenbank. Überprüfen sie Link, Benutzer, Passwort und ausgewählte Datenbank', ex)

        print("databaseConnection aufruf")

    def getVehicles(self):
        global cursor
        global numrows
        global numrows2
        global numrows3
        global numrows4

        self.databaseConnection()

        cursor = db.cursor()

        cursor.execute("SELECT * FROM Fahrzeug WHERE Fahrzeugtyp = 'RTW'")
        numrows2 = cursor.rowcount
    
        cursor.execute("SELECT * FROM Fahrzeug WHERE Fahrzeugtyp = 'KTW'")
        numrows3 = cursor.rowcount

        cursor.execute("SELECT * FROM Fahrzeug WHERE Fahrzeugtyp = 'NEF'")
        numrows4 = cursor.rowcount

        # Execute SQL select statement
        cursor.execute("SELECT * FROM Fahrzeug")
        # Get the number of rows in the resultset
        numrows = cursor.rowcount

        print("getVehicles aufruf")

def main():
    global app
    global ex

    app = QApplication(sys.argv)
    print("app = QAPP")
    ex = App()
    print("ex=APP()")
    ex.update()
    print("ex.update()")
    sys.exit(app.exec_())
    print("sys.exit")  
    db.close()

if __name__ == '__main__':
    main()




"""if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("app = QAPP")
    ex = App()
    print("ex=APP()")
    ex.update()
    print("ex.update()")
    sys.exit(app.exec_())
    print("sys.exit")  
    db.close()

"""