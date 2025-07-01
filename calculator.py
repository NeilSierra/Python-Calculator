import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        pass

if __name__ == "__main__":
    app = QApplication()
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())