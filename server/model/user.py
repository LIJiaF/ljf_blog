from sqlalchemy import Column, String, Integer, Sequence
from .orm_base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
