import hashlib
import random
import string

from cryptacular.bcrypt import BCRYPTPasswordManager

from sqlalchemy import (
    Column,
    Integer,
    String,
    Unicode,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    backref,
    relationship,
    scoped_session,
    sessionmaker,
    synonym,
    )

from sqlalchemy.schema import ForeignKey

from zope.sqlalchemy import ZopeTransactionExtension

from apex.models import AuthID

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
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
    paypal_email = Column(String(120))
    twilio_sid = Column(String(120))
    twilio_number = Column(String(120))

    user = relationship(AuthID, backref=backref('profile', uselist=False))

class MailboxGreeting(Base):
    __tablename__ = 'mailbox_greetings'

    id = Column(Integer, primary_key=True)
    shelter_phone = Column(Unicode(24))
    mailbox = Column(Integer)
    url = Column(String(120))
    salt = Column(Unicode(24))
    _password = Column('password', Unicode(80), default=u'')

    def _set_password(self, password):
        self.salt = self.get_salt(24)
        password = password + self.salt
        self._password = BCRYPTPasswordManager().encode(password, rounds=12)

    def _get_password(self):
        return self._password

    password = synonym('_password', descriptor=property(_get_password, \
                       _set_password))

    def get_salt(self, length):
        m = hashlib.sha256()
        word = ''

        for i in xrange(length):
            word += random.choice(string.ascii_letters)

        m.update(word)

        return unicode(m.hexdigest()[:length])

    @classmethod
    def check_password(cls, **kwargs):
        if kwargs.has_key('id'):
            user = cls.get_by_id(kwargs['id'])

        try:
            if BCRYPTPasswordManager().check(user.password,
                '%s%s' % (kwargs['password'], user.salt)):
                return True
        except TypeError:
            pass
