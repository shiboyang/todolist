# @Time    : 2021/9/7 22:23
# @Author  : Boyang
# @Site    : 
# @File    : window.py
# @Software: PyCharm
import random

from PyQt5 import QtWidgets
from PyQt5 import QtCore

from apps import get_session
from apps.models import ModelBoard
from ui.window import Ui_MainWindow
from apps.modules.board import Board


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)
        self.setupUi(self)
        self.btn_add_task.clicked.connect(self.add_board_clicked)
        self.init_main_widget()

    def init_main_widget(self):
        with get_session() as session:
            for mb in session.query(ModelBoard).filter(ModelBoard.is_delete.is_(False)):
                self.layout_boards.addWidget(Board.from_model(self.scrollAreaWidgetContents, mb))

    def add_board_clicked(self):
        """
        添加看板
        :return:
        """
        board = Board.create_board(self.scrollAreaWidgetContents)
        if board:
            self.layout_boards.addWidget(board)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
