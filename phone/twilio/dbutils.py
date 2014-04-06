from phone.models import (DBSession,
                          MailboxGreeting)

def get_mailbox_url(shelter_phone, mailbox_number):
    return DBSession.query(MailboxGreeting) \
        .filter(MailboxGreeting.shelter_phone==shelter_phone) \
        .filter(MailboxGreeting.mailbox==mailbox_number).first() 

def create_mailbox(shelter_phone, mailbox_number):
    print 'creating mailbox', mailbox_number
    mailbox = MailboxGreeting(shelter_phone=shelter_phone,
        mailbox=mailbox_number)
    DBSession.add(mailbox)
    DBSession.flush()

def update_mailbox(shelter_phone, mailbox_number, url):
    mailbox = DBSession.query(MailboxGreeting) \
        .filter(MailboxGreeting.shelter_phone==shelter_phone) \
        .filter(MailboxGreeting.mailbox==mailbox_number).first() 
    mailbox.url = url
    DBSession.merge(mailbox)
    DBSession.flush()

def update_mailbox_password(shelter_phone, mailbox_number, password):
    mailbox = DBSession.query(MailboxGreeting) \
        .filter(MailboxGreeting.shelter_phone==shelter_phone) \
        .filter(MailboxGreeting.mailbox==mailbox_number).first() 
    mailbox.password = password
    DBSession.merge(mailbox)
    DBSession.flush()
