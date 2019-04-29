import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        #Konstruktor von QMainwindow aufrufen
        super().__init__()

        #Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(800, 600))
        self.setWindowTitle('IUK Management')

        #Title-Widget erzeugen und in Fenster einbetten
        title = QLabel('IUK Management', self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(title)

#Fenster öffnen; das Programm läuft, bis das Fenster geschlossen wird
app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
