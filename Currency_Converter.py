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


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("converter.ui", self)
        self.button.clicked.connect((lambda: self.convert_calc(self.showinput(), self.showoutput(), self.takeinput())))
        self.label.hide()
        self.label.setWordWrap(True)
        icon = (QIcon("icon.png"))
        self.setWindowIcon(icon)
        self.setWindowTitle("Currency Calculator")


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


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
try:
    sys.exit(app.exec())
except SystemExit:
    print("Closing Window")

