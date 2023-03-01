import sys
from unittest import result
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

#-----Basic Calculator------

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,400,250)
        self.initUI()
        
    def initUI(self):


        self.label =QtWidgets.QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)
        self.label.setWordWrap(True) #multiline true

        self.lbl_number1=QtWidgets.QLabel(self)
        self.lbl_number1.setText("Number 1: ")
        self.lbl_number1.move(40,30)

        self.txt_number1=QtWidgets.QLineEdit(self)
        self.txt_number1.move(150,30)
        self.txt_number1.resize(200,32)

        self.lbl_number2=QtWidgets.QLabel(self)
        self.lbl_number2.setText("Number 2: ")
        self.lbl_number2.move(40,80)
       
        self.txt_number2=QtWidgets.QLineEdit(self)
        self.txt_number2.move(150,80)
        self.txt_number2.resize(200,32)

        self.lbl_result=QtWidgets.QLabel(self)      
        self.lbl_result.move(150,180)

        btn_plus=QtWidgets.QPushButton(self)
        btn_plus.setText("+")
        btn_plus.resize(40,40)
        btn_plus.move(150,130)
        btn_plus.clicked.connect(self.calculate)

        btn_minus=QtWidgets.QPushButton(self)
        btn_minus.setText("-")
        btn_minus.resize(40,40)
        btn_minus.move(190,130)
        btn_minus.clicked.connect(self.calculate)

        btn_multiply=QtWidgets.QPushButton(self)
        btn_multiply.resize(40,40)
        btn_multiply.setText("X")
        btn_multiply.move(230,130)
        btn_multiply.clicked.connect(self.calculate)
        
        btn_divided=QtWidgets.QPushButton(self)
        btn_divided.resize(40,40)
        btn_divided.setText("/")
        btn_divided.move(270,130)
        btn_divided.clicked.connect(self.calculate)

        del_btn=QtWidgets.QPushButton(self)
        del_btn.resize(40,40)
        del_btn.move(310,130)
        del_btn.setText("C")
        del_btn.clicked.connect(self.calculate)

    
    def calculate(self):
        sender=self.sender()
        result=0

        if sender.text() == "+":
            result= int(self.txt_number1.text())+ int(self.txt_number2.text())
        elif sender.text() == "-":
            result= int(self.txt_number1.text())- int(self.txt_number2.text())
        elif sender.text() =="X":
            result= int(self.txt_number1.text())* int(self.txt_number2.text())
        elif sender.text() =="/" : 
            result= int(self.txt_number1.text())/ int(self.txt_number2.text())
        elif sender.text() == "C":
            self.lbl_result.setText("")
        
        self.lbl_result.setText("Result: "+ str(result))


def app():
    app=QApplication(sys.argv)
    win=MainForm()
    win.show()
    sys.exit(app.exec_())

app()