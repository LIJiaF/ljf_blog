from sqlalchemy import Column, String, Integer, Text, DateTime, Sequence
from .orm_base import Base


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, Sequence('article_id_seq'), primary_key=True)
    title = Column(String(50))
    author = Column(String(30))
    content = Column(Text)
    create_date = Column(DateTime)
    write_date = Column(DateTime)
