import sys
from PySide6 import QtWidgets as qtw

from App_Main.app_main import AppMain

if __name__ == "__main__":
    # Creates the app
    app = qtw.QApplication(sys.argv)

    # Opens the main window
    window = AppMain()

    sys.exit(app.exec())