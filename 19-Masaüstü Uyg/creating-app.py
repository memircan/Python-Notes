import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QToolTip
#from PyQt5.QtGui import QIcon  #pencere solüst köseye icon koymak icin


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First App") #pencere baslıgı
    win.setGeometry(200,200,500,500) #ilk 2 veri konum, son 2 veri ise boyut
    #win.setWindowIcon(QIcon("logo.png")) 
    win.setToolTip("my tooltip") 


    win.show()
    sys.exit(app.exec_()) #çarpıya basınca uyg kapanması

window()