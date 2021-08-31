from .Database import Base
from sqlalchemy import String, Text, Integer, Column


class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    name = Column(String(255),nullable=False,unique=True)
    description = Column(Text)
