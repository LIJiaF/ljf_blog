from sqlalchemy import Column, Sequence, String, Integer, Text, DateTime, ForeignKey
from .orm_base import Base


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, Sequence('article_id_seq'), primary_key=True)
    image_url = Column(String)
    title = Column(String)
    author = Column(String)
    content = Column(Text)
    class_id = Column(Integer, ForeignKey('article_class.id'))
    create_date = Column(DateTime)
    write_date = Column(DateTime)
