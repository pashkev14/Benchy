from PySide6 import QtWidgets, QtCore
import sys


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.resize(400, 300)

        self.text = QtWidgets.QLabel("Hello, world!", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.setWindowTitle('Hello')
    window.show()
    sys.exit(app.exec())
