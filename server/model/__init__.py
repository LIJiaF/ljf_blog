from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import pgsqlConfig
from .orm_base import Base
from .article import Article
from .article_class import ArticleClass

# 初始化数据库连接:
conn_str = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'.format(**pgsqlConfig)
engine = create_engine(conn_str, pool_size=100, max_overflow=0)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    create_table()
    drop_table()
