import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QFrame, QVBoxLayout, QGridLayout, QSizePolicy

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.displayFrame = QFrame()
        self.buttonsFrame = QFrame()
        self.addButton = QPushButton("+", self)
        self.subButton = QPushButton("-", self)
        self.mulButton = QPushButton("×", self)
        self.divButton = QPushButton("÷", self)
        self.modButton = QPushButton("%", self)
        self.expButton = QPushButton("^", self)
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
        self.initUI()

    def initUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        centralWidget.setObjectName("centralWidget")
        self.displayFrame.setObjectName("displayFrame")
        self.buttonsFrame.setObjectName("buttonsFrame")

        self.setGeometry(0, 0, 500, 750)
        self.setWindowTitle("Calculator")
        centralWidget.setStyleSheet(
        """
            QWidget#centralWidget {
                padding: 10px;
                background-color: #202020;
            }

            QFrame#displayFrame {
                background-color: white;
            }

            QFrame#buttonsFrame {
                margin: 0;
                background-color: white;
            }
        """)

        for btn in [
            self.addButton, self.subButton, self.mulButton, self.divButton,
            self.modButton, self.expButton, self.eqlButton, self.decButton,
            self.num1Button, self.num2Button, self.num3Button, self.num4Button,
            self.num5Button, self.num6Button, self.num7Button, self.num8Button,
            self.num9Button, self.num0Button, self.delButton, self.clrButton
        ]:
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

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
        buttonsLayout.addWidget(self.modButton, 1, 3)
        self.buttonsFrame.setLayout(buttonsLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())