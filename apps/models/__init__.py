# @Time    : 2021/9/14 13:42
# @Author  : Boyang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
import time

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from apps.utils import gen_key, human_timestamp

ModelBase = declarative_base()


class ModelBoard(ModelBase):
    __tablename__ = 'board'
    id = Column(String(32), primary_key=True, default=gen_key)
    title = Column(String(32), nullable=False)
    create_time = Column(Integer, default=human_timestamp)
    is_delete = Column(Boolean, default=False, comment='')
    tasks = relationship('ModelTask', uselist=True,
                         primaryjoin='and_(ModelTask.board_id==ModelBoard.id, ModelTask.is_delete.is_(False))')

    def __repr__(self):
        return '<ModelBoard %r>' % self.id


class ModelTask(ModelBase):
    __tablename__ = 'task'
    id = Column(String(32), primary_key=True, default=gen_key)
    detail = Column(String(512), nullable=False)
    desc = Column(String(255), nullable=True)
    notify_time = Column(Integer, nullable=True)
    create_time = Column(Integer, default=human_timestamp)
    board_id = Column(String(32), ForeignKey('board.id'))
    is_delete = Column(Boolean, default=False)
    # board = relationship('ModelBoard')

# from sqlalchemy import create_engine
# from apps.conf import config
#
# _engine = create_engine(config.DATABASE_URL)
# ModelBase.metadata.create_all(bind=_engine)
