import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from error import Ui_MainWindow


class ErrorForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.close_form)

    def close_form(self):
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ErrorForm()
    ex.show()
    sys.exit(app.exec())