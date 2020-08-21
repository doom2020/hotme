from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
from tornado.options import options

pymysql.install_as_MySQLdb()

# 连接数据库格式
# mysql+pymysql://root:123456@127.0.0.1:3306/hotme
db_url = "mysql://root:123456@127.0.0.1:3306/hotme"
# db_url = "mysql://%s:%s@%s:%s/%s" % (options.db_user, options.db_password, options.db_host, options.db_port,\
#                                      options.db_name)

# 创建引擎，建立连接
engine = create_engine(db_url)

# 模型数据库关联基类
Base = declarative_base(bind=engine)

# 创建DBSession类
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()
