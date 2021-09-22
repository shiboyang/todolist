# @Time    : 2021/9/15 11:23
# @Author  : Boyang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
import time
from uuid import uuid4


def gen_key():
    return uuid4().hex


def human_timestamp():
    return int(time.time())
