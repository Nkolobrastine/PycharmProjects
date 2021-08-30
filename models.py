from sqlalchemy.orm import Base
from Database import Base
from sqlalchemy import String, Text, Integer, Column,Boolean,ForeignKey


class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False , unique= True)
    description = Column(Text)
