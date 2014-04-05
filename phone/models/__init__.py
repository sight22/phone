from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)

class Shelter(Base):
    __tablename__ = 'shelters'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    address_1 = Column(String(120))
    address_2 = Column(String(120))
    city = Column(String(120))
    state = Column(String(120))
    zip = Column(Integer)
