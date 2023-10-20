import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import requests

url = "https://api.frankfurter.app/latest"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    rates = data["rates"]
else:
    print("Invalid API error")
# API(the program takes information from this api using the Requests library)


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("converter.ui", self)  # yes i use pycharm
        self.button.clicked.connect((lambda: self.convert_calc(self.showinput(), self.showoutput(), self.takeinput())))
        self.label.hide()
        self.label.setWordWrap(True)
        icon = (QIcon("icon.png"))
        self.setWindowIcon(icon)
        self.setWindowTitle("Currency Calculator")
# PyQt6 stuff. If you don't know PyQt6, it is normal that you don't understand these. There are PyQt6 tutorials on YouTube.
# Here is a horrible explanation of what this code does.
# We make a new class and add QMainWindows's features into it.
# uic.loadUi takes and loads information from an ui file made with PyQt6 designer.
# The ui file has the general properties of the window(button, label etc. and their positions, size...).
# self.label.hide hides the error message if there is no error
# self.button.clicked.connect runs the function I defined below when the button is pressed.

    def takeinput(self):
        return self.input.text()

    def showinput(self):
        return self.inputype.currentText()

    def showoutput(self):
        return self.comboBox_2.currentText()

    def showresult(self, end):
        self.output.setText(str(end))

    def convert_calc(self, x, y, z):
        try:
            z = float(z)
            self.label.hide()
        except ValueError:
            self.label.show()
            z = 0
        rates["EUR"] = 1
        if x == "EUR":
            result = z * rates[y]
            self.showresult(result)
        else:
            new_value = z * (1 / rates[x])
            result = new_value * rates[y]
            self.showresult(result)
# Functions are self-explanatory. Most of them collect information for convert_calc function.
# convert_calc function takes the information, calculates and outputs the result(via showresult function)


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
try:
    sys.exit(app.exec())
except SystemExit:
    print("Closing Window")
# These make it so the window can open and close properly
