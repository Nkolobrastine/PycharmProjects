from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine ("postgresql://brastine:scott@localhost:5432/Todo_db", echo=True)

Base = declarative_base ()
SessionLocal = sessionmaker (bind=engine)