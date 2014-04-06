from phone.models import (DBSession,
                          MailboxGreeting)

def get_mailbox_url(mailbox_number):
    return DBSession.query(MailboxGreeting) \
        .filter(MailboxGreeting.mailbox==mailbox_number).first() 
