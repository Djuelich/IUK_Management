< import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        global txts

        #Konstruktor von QMainwindow aufrufen
        super().__init__()

        #Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(800, 600))
        self.setWindowTitle('IUK Management')

        #GridLayout für Widget in Main-Window (Layout von MAin-Window kann nicht verändert werden)

#Fenster öffnen; das Programm läuft, bis das Fenster geschlossen wird
app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
