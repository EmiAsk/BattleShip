from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
import sys


class ErrorForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Error')
        self.resize(655, 275)

        self.label = QLabel(
            "The operation was not completed successfully. \n Read the rules carefully and try again.",
            self)
        self.label.setGeometry(140, 60, 531, 71)
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.label_cross = QLabel("⊗", self)
        self.label_cross.setGeometry(60, 50, 111, 91)
        self.label_cross.setStyleSheet("font: 72pt \"MS Shell Dlg 2\";color: rgb(255, 0, 0);")

        self.button_ok = QPushButton('OK', self)
        self.button_ok.setGeometry(250, 180, 131, 51)
        self.button_ok.clicked.connect(self.close_form)

    def close_form(self):
        exit()


def main():
    app = QApplication(sys.argv)
    form = ErrorForm()
    form.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
