# @Time    : 2021/8/26 14:06
# @Author  : Boyang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
import logging
import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, Session
from sqlalchemy.orm import sessionmaker

from apps.conf import config

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

_engine = create_engine(config.DATABASE_URL)
_session_factory = sessionmaker(bind=_engine, autocommit=False, autoflush=False)


@contextmanager
def get_session() -> Session:
    s_session = scoped_session(_session_factory)
    _session = s_session()
    yield _session
    try:
        _session.commit()
    except Exception as e:
        logger.info(f'database error: {e}')
        _session.rollback()
