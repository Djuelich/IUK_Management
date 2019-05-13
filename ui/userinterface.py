import sys
from PyQT5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainwindow, QLabel, QWidget
from PyQt5.QtCore import QSize

class Mainwindow(QMainwindow):
    def __init__(self):
        #Konstruktor von QMainwindow aufrufen
        super().__init__()

        #Fenstergröße und Titel einstellen
        self.setMinimumSize(Qsize(800, 600))
        self.setWindowTitle('IUK Management')

        #Title-Widget erzeugen und in Fenster einbetten
        title = QLabel('IUK Management', self)
        title.setAlignment(QTCore.QT.AlignCenter)

#Fenster öffnen; das Programm läuft, bis das Fenster geschlossen wird
app = QTWidget.QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
