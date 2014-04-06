from phone.models import (DBSession,
                          MailboxGreeting)

def get_mailbox_url(mailbox_number):
    return DBSession.query(MailboxGreeting) \
        .filter(MailboxGreeting.mailbox==mailbox_number).first() 

def create_mailbox(mailbox_number):
    print 'creating mailbox', mailbox_number
    mailbox = MailboxGreeting(mailbox=mailbox_number)
    DBSession.add(mailbox)
    DBSession.flush()
