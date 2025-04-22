import sys


from PyQt6 import QtWidgets
from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QApplication

from frontend import controller
from frontend.main_window import Ui_MainWindow


#Основной метод приложения

def make_application():
    app = QApplication(sys.argv)

    items = controller.load_items()

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.show_items(items)

    MainWindow.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    make_application()