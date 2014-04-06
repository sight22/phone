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
    relationship,
    backref
    )

from sqlalchemy.schema import ForeignKey

from apex.models import AuthID

DBSession = scoped_session(sessionmaker(autocommit=True))
Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelters'

    id = Column(Integer, primary_key=True)
    auth_id = Column(Integer, ForeignKey(AuthID.id), index=True)
    name = Column(String(32))
    address_1 = Column(String(120))
    address_2 = Column(String(120))
    city = Column(String(120))
    state = Column(String(120))
    zip = Column(Integer)

    #user = relationship(AuthID, backref=backref('profile', uselist=False))
