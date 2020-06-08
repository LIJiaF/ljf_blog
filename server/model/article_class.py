from sqlalchemy import Column, Sequence, String, Integer, DateTime
from .orm_base import Base


class ArticleClass(Base):
    __tablename__ = 'article_class'

    id = Column(Integer, Sequence('article_class_id_seq'), primary_key=True)
    name = Column(String)
    create_date = Column(DateTime)
    write_date = Column(DateTime)
