import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load trực tiếp file .ui
        uic.loadUi("main.ui", self)

        self.pushButton.clicked.connect(self.handleClick)

    def handleClick(self):
        self.label.setText("Hello PyQt6!")

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())