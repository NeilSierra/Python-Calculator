import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, QLabel, QFrame,
                             QVBoxLayout, QGridLayout, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.displayFrame = QFrame()
        self.buttonsFrame = QFrame()
        self.addButton = QPushButton("+", self)
        self.subButton = QPushButton("-", self)
        self.mulButton = QPushButton("*", self)
        self.divButton = QPushButton("/", self)
        self.opnParButton = QPushButton("(", self)
        self.clsParButton = QPushButton(")", self)
        self.eqlButton = QPushButton("=", self)
        self.decButton = QPushButton(".", self)
        self.num1Button = QPushButton("1", self)
        self.num2Button = QPushButton("2", self)
        self.num3Button = QPushButton("3", self)
        self.num4Button = QPushButton("4", self)
        self.num5Button = QPushButton("5", self)
        self.num6Button = QPushButton("6", self)
        self.num7Button = QPushButton("7", self)
        self.num8Button = QPushButton("8", self)
        self.num9Button = QPushButton("9", self)
        self.num0Button = QPushButton("0", self)
        self.delButton = QPushButton("Del", self)
        self.clrButton = QPushButton("Clr", self)
        self.equationLabel = QLabel("", self)
        self.resultLabel = QLabel("", self)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 750)
        self.setWindowTitle("Basic Calculator")
        self.setWindowIcon(QIcon("icon.png"))

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        centralWidget.setObjectName("centralWidget")
        self.displayFrame.setObjectName("displayFrame")
        self.buttonsFrame.setObjectName("buttonsFrame")

        centralWidget.setStyleSheet(
        """
            QWidget#centralWidget {
                padding: 10px;
                background-color: #202020;
            }

            QPushButton {
                background-color: #3B3B3B;
                border-radius: 10px;
                font-size: 32px;
                font-family: 'Calibri';
                font-weight: Bold;
                color: #FFFFFF;
            }

            QPushButton:hover {
                background-color: #545454;
            }

            QLabel {
                font-size: 64px;
                font-family: 'Calibri';
                color: #FFFFFF;
            }
        """)

        for button in [
            self.addButton, self.subButton, self.mulButton, self.divButton, self.opnParButton, self.clsParButton, self.eqlButton, self.decButton, self.num1Button, self.num2Button, self.num3Button, self.num4Button, self.num5Button, self.num6Button, self.num7Button, self.num8Button, self.num9Button, self.num0Button, self.delButton, self.clrButton
        ]:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setCursor(Qt.PointingHandCursor)

        self.equationLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.resultLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(10)
        mainLayout.addWidget(self.displayFrame)
        mainLayout.addWidget(self.buttonsFrame)
        mainLayout.setStretch(0, 200)
        mainLayout.setStretch(1, 520)
        centralWidget.setLayout(mainLayout)

        buttonsLayout = QGridLayout()
        buttonsLayout.setSpacing(10)
        buttonsLayout.setContentsMargins(0, 0, 0, 0)
        buttonsLayout.addWidget(self.addButton, 0, 0)
        buttonsLayout.addWidget(self.subButton, 0, 1)
        buttonsLayout.addWidget(self.mulButton, 0, 2)
        buttonsLayout.addWidget(self.divButton, 0, 3)
        buttonsLayout.addWidget(self.num7Button, 1, 0)
        buttonsLayout.addWidget(self.num8Button, 1, 1)
        buttonsLayout.addWidget(self.num9Button, 1, 2)
        buttonsLayout.addWidget(self.opnParButton, 1, 3)
        buttonsLayout.addWidget(self.num4Button, 2, 0)
        buttonsLayout.addWidget(self.num5Button, 2, 1)
        buttonsLayout.addWidget(self.num6Button, 2, 2)
        buttonsLayout.addWidget(self.clsParButton, 2, 3)
        buttonsLayout.addWidget(self.num1Button, 3, 0)
        buttonsLayout.addWidget(self.num2Button, 3, 1)
        buttonsLayout.addWidget(self.num3Button, 3, 2)
        buttonsLayout.addWidget(self.delButton, 3, 3)
        buttonsLayout.addWidget(self.num0Button, 4, 0)
        buttonsLayout.addWidget(self.decButton, 4, 1)
        buttonsLayout.addWidget(self.eqlButton, 4, 2)
        buttonsLayout.addWidget(self.clrButton, 4, 3)
        self.buttonsFrame.setLayout(buttonsLayout)

        displayLayout = QVBoxLayout()
        displayLayout.setSpacing(0)
        displayLayout.setContentsMargins(0, 0, 0, 0)
        displayLayout.addWidget(self.equationLabel)
        displayLayout.addWidget(self.resultLabel)
        self.displayFrame.setLayout(displayLayout)

        for button in [
            self.addButton, self.subButton, self.mulButton, self.divButton, self.opnParButton, self.clsParButton, self.decButton, self.num1Button, self.num2Button, self.num3Button, self.num4Button, self.num5Button, self.num6Button, self.num7Button, self.num8Button, self.num9Button, self.num0Button
        ]:
            button.clicked.connect(self.on_click)

        self.delButton.clicked.connect(self.on_delete)
        self.clrButton.clicked.connect(self.on_clear)
        self.eqlButton.clicked.connect(self.on_equal)
    
    def on_click(self):
        char = self.sender().text()
        equation = self.equationLabel.text() + char
        self.equationLabel.setText(equation)
    
    def on_clear(self):
        self.equationLabel.setText("")
        self.resultLabel.setText("")

    def on_delete(self):
        equation = self.equationLabel.text()
        equation = equation[:-1]
        self.equationLabel.setText(equation)

    def on_equal(self):
        equation = self.equationLabel.text()

        try:
            result = eval(equation)
        except SyntaxError:
            self.resultLabel.setText("SyntaxError")
        except ZeroDivisionError:
            self.resultLabel.setText("ZeroDivisionError")
        else:
            self.resultLabel.setText(f"= {result}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    calculator = Calculator()
    calculator.show()

    frameGeometry = calculator.frameGeometry()
    screen = app.primaryScreen()
    center = screen.availableGeometry().center()
    frameGeometry.moveCenter(center)
    calculator.move(frameGeometry.topLeft())

    sys.exit(app.exec_())