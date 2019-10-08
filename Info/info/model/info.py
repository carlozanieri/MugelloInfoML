# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relation, backref
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime

from info.model import DeclarativeBase, metadata, DBSession
from datetime import datetime

class WikiPage(DeclarativeBase):
    __tablename__ = 'wiki_page'

    uid = Column(Integer, primary_key=True)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    title = Column(Unicode(255), nullable=False, unique=True)
    data = Column(Unicode(4096), nullable=False, default='')