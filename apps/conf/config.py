# @Time    : 2021/9/14 15:57
# @Author  : Boyang
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os

current_path = os.path.dirname(os.path.abspath(__file__))

DATABASE_URL = f'sqlite:///{os.path.join(os.path.dirname(os.path.dirname(current_path)), "data/todolist.db")}'
print(current_path)