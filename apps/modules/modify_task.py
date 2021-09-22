# @Time    : 2021/9/11 17:17
# @Author  : Boyang
# @Site    : 
# @File    : modify_task.py
# @Software: PyCharm
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from ui.modify_task import Ui_ModifyTask


class Task(QtWidgets.QDialog, Ui_ModifyTask):
    def __init__(self, parent=None):
        super(Task, self).__init__(parent=parent)
        self.setupUi(self)

        self.btn_modify.clicked.connect(self.close())
        self.btn_cancel.clicked.connect(self.close())
