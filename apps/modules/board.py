# @Time    : 2021/9/8 14:54
# @Author  : Boyang
# @Site    : 
# @File    : board.py
# @Software: PyCharm
from PyQt5 import QtWidgets
from ui.board import Ui_Board
from apps.modules.board_item import BoardItem
from apps.models import ModelBoard
from apps import get_session


class Board(QtWidgets.QWidget, Ui_Board):
    id = None

    def __init__(self, parent=None):
        super(Board, self).__init__(parent=parent)
        self.setupUi(self)
        self._init_widget()
        self.btn_open_add.clicked.connect(self.btn_open_add_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.widget_4.setVisible(False)

    def _init_widget(self):
        menu_bar = QtWidgets.QMenuBar()
        menu_bar.setMaximumWidth(30)
        menu_bar.setMaximumHeight(22)
        pop_menu = QtWidgets.QMenu(menu_bar)
        add_task_menu_item = pop_menu.addAction('添加任务')
        add_task_menu_item.triggered.connect(self.btn_open_add_clicked)
        remove_task_menu_item = pop_menu.addAction('删除这个看板')
        remove_task_menu_item.triggered.connect(self.remove_board_triggered)

        pop_menu.setTitle("  ")
        menu_bar.addAction(pop_menu.menuAction())
        self.horizontalLayout_2.addWidget(menu_bar)

    def remove_board_triggered(self):
        with get_session() as session:
            board = session.query(ModelBoard).filter(ModelBoard.id == self.id).one_or_none()
            board.is_delete = True
            session.add(board)
        self.close()

    @classmethod
    def create_board(cls, parent):
        board_title, ok = QtWidgets.QInputDialog().getText(parent, '提示', '请输入标题:')
        if ok and board_title:
            board = cls(parent)
            board.lab_title.setText(board_title)
            with get_session() as session:
                mb = ModelBoard()
                mb.title = board_title
                session.add(mb)
            board.id = mb.id
            return board

    @classmethod
    def from_model(cls, parent, model: ModelBoard):
        board = cls(parent)
        board.lab_title.setText(model.title)
        board.lab_task_count.setText(str(len(model.tasks)))
        board.id = model.id
        for task in model.tasks:
            item = BoardItem.from_model(board, task)
            board.layout_task_items.addWidget(item)

        return board

    def btn_open_add_clicked(self):
        self.widget_4.setVisible(not self.widget_4.isVisible())

    def btn_add_clicked(self):
        board_item = BoardItem.create_item(parent=self.scrollAreaWidgetContents_2, board_id=self.id,
                                           task_detail=self.pte_task_detail.toPlainText(),
                                           notify=self.ckb_notify.isChecked(),
                                           notify_time=self.dte_notfify.dateTime().toPyDateTime().timestamp())
        self.layout_task_items.addWidget(board_item)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    board = Board()
    board.show()

    sys.exit(app.exec_())
