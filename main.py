from gui.app import MyApp
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
