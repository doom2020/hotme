from sqlalchemy import Column, String, Integer

from utils.conn import Base


class UserInfo(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=True)
    phone = Column(String(15), unique=True, nullable=True)
    password = Column(String(50), nullable=True)

    __tablename__ = 'user_info'