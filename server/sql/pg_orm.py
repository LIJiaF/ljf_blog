from sqlalchemy import Column, String, Integer, Sequence, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import pgsqlConfig

# 初始化数据库连接:
conn_str = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'.format(**pgsqlConfig)
engine = create_engine(conn_str, echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建对象的基类:
Base = declarative_base()


Base.metadata.create_all(engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User()
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
