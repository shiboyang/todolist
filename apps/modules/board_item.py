# @Time    : 2021/9/10 13:25
# @Author  : Boyang
# @Site    : 
# @File    : board_item.py
# @Software: PyCharm
import datetime

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from apps import get_session
from ui.board_item import Ui_BoardItem
from apps.models import ModelTask


class BoardItem(Ui_BoardItem, QtWidgets.QWidget):
    id = None

    def __init__(self, parent=None):
        super(BoardItem, self).__init__(parent=parent)
        self.setupUi(self)
        self._init_widget()

    def _init_widget(self):
        menu_bar = QtWidgets.QMenuBar()
        menu_bar.setMaximumWidth(30)
        menu_bar.setMaximumHeight(22)
        pop_menu = QtWidgets.QMenu(menu_bar)
        pop_menu.addAction('编辑')
        remove_menu = pop_menu.addAction('删除')
        remove_menu.triggered.connect(self.destroy_item)
        menu_bar.addAction(pop_menu.menuAction())
        pop_menu.setTitle('···')
        self.lat_menu.addWidget(menu_bar)

    def destroy_item(self):
        with get_session() as session:
            task = session.query(ModelTask).filter(ModelTask.id == self.id).one_or_none()
            task.is_delete = True
            session.add(task)
        self.close()

    @classmethod
    def create_item(cls, parent, board_id, task_detail, notify, notify_time):
        with get_session() as session:
            mt = ModelTask()
            mt.board_id = board_id
            mt.detail = task_detail
            if notify:
                mt.notify_time = notify_time
            session.add(mt)

        return cls.from_model(parent, mt)

    @classmethod
    def from_model(cls, parent, model: ModelTask):
        item = cls(parent)
        item.pte_detail.setPlainText(model.detail)
        create_time = datetime.datetime.fromtimestamp(model.create_time).strftime('%Y%m%d %H:%M:%S')
        notify_time = datetime.datetime.fromtimestamp(model.notify_time).strftime(
            '%Y%m%d %H:%M:%S') if model.notify_time else ''
        item.lab_create_time.setText(create_time)
        item.lab_notify_time.setText(notify_time)

        item.id = model.id
        return item

    def modify_task(self):
        pass
