import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QVBoxLayout

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        layout = QVBoxLayout()
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def handle_login(self):
        # Simulate successful login
        self.accept()  # This closes the dialog with an accepted state

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 600, 400)

        self.button = QPushButton("Logout", self)
        self.button.clicked.connect(self.close)

        self.setCentralWidget(self.button)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_dialog = LoginDialog()
    if login_dialog.exec() == QDialog.accepted:
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec())