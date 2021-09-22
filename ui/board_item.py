# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'board_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BoardItem(object):
    def setupUi(self, BoardItem):
        BoardItem.setObjectName("BoardItem")
        BoardItem.resize(302, 213)
        BoardItem.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(BoardItem)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pte_detail = QtWidgets.QPlainTextEdit(BoardItem)
        self.pte_detail.setMinimumSize(QtCore.QSize(0, 0))
        self.pte_detail.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pte_detail.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.pte_detail.setReadOnly(True)
        self.pte_detail.setPlainText("")
        self.pte_detail.setObjectName("pte_detail")
        self.verticalLayout.addWidget(self.pte_detail)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(BoardItem)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lab_notify_time = QtWidgets.QLabel(BoardItem)
        self.lab_notify_time.setObjectName("lab_notify_time")
        self.horizontalLayout_2.addWidget(self.lab_notify_time)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(BoardItem)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lab_create_time = QtWidgets.QLabel(BoardItem)
        self.lab_create_time.setObjectName("lab_create_time")
        self.horizontalLayout.addWidget(self.lab_create_time)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lat_menu = QtWidgets.QHBoxLayout()
        self.lat_menu.setObjectName("lat_menu")
        self.verticalLayout_4.addLayout(self.lat_menu)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(BoardItem)
        QtCore.QMetaObject.connectSlotsByName(BoardItem)

    def retranslateUi(self, BoardItem):
        _translate = QtCore.QCoreApplication.translate
        BoardItem.setWindowTitle(_translate("BoardItem", "Form"))
        self.label.setText(_translate("BoardItem", "提醒:"))
        self.lab_notify_time.setText(_translate("BoardItem", "None"))
        self.label_2.setText(_translate("BoardItem", "创建时间:"))
        self.lab_create_time.setText(_translate("BoardItem", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BoardItem = QtWidgets.QWidget()
    ui = Ui_BoardItem()
    ui.setupUi(BoardItem)
    BoardItem.show()
    sys.exit(app.exec_())
