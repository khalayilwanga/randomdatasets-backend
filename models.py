from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Entry(Base):
    __tablename__ = 'entries'
    id = Column('id',Integer,primary_key=True, autoincrement=True)
    value = Column('value',Integer,nullable=False)

class Colors(Base):
    __tablename__ = 'colores'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    red= Column('red',Integer,nullable=False)
    blue= Column('blue',Integer,nullable=False)
    green = Column('green', Integer, nullable=False)
    alpha = Column('alpha', Integer, nullable=False)


