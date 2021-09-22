# @Time    : 2021/9/14 17:38
# @Author  : Boyang
# @Site    : 
# @File    : run.py
# @Software: PyCharm
import sys

from PyQt5 import QtWidgets

from apps.modules.window import Window


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
