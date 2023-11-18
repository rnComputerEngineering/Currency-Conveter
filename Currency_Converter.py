import os.path
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import requests

executable_path = os.path.dirname(os.path.abspath(__file__))
executable_path = os.path.join(executable_path,"uifiles")
first_ui = os.path.join(executable_path, "error_message.ui")
second_ui = os.path.join(executable_path, "converter.ui")
print(second_ui)


class ErrorMessage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(f"{first_ui}", self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(second_ui, self)
        self.button.clicked.connect((lambda: self.convert_calc(self.showinput(), self.showoutput(), self.takeinput())))
        self.label.hide()
        self.label.setWordWrap(True)
        self.setWindowTitle("Currency Converter")

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


url = "https://api.frankfurter.app/latest"
try:
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        pass


except requests.RequestException:
    app = QApplication(sys.argv)
    window = ErrorMessage()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        pass

