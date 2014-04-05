phone
=====

Built directly with:

* https://github.com/Qwait/python-temboo

Built indirectly with:

* https://github.com/duointeractive/paypal-python/
* https://github.com/sendgrid/sendgrid-python
* https://github.com/twilio/twilio-python


Homeless shelter signs up with Twilio (can we do this through temboo) and
receives a twimlet URL

Homeless shelter can create their own greeting?

Voicemail Flow:

Welcome to ShelterPhone, please enter the 4 digit mailbox number you're trying
to reach or * for a menu of options.

1234 -> Play greeting, take message

* -> Press 1 to create a new mailbox
     Press 2 to administer the system

1 -> Welcome to the voicemail system. Please select a 4 digit number between 1000 and 9999.

Please select a 4 digit password.
Please reenter your password.
Please record a greeting.
Your voice mailbox of xxxx has been set up. The phone number you can use to retrieve your messages is xxx-xxx-xxxx. Again that number is xxx-xxx-xxxx. Your mailbox number is xxxx. Again, your mailbox number is xxxx. (repeat 3 times)

2 -> statistics there are xxxx mailboxes, xxxx which have messages waiting that
haven't been accessed in 60 days. xxxx which have no messages. Press * to delete 
the inactive accounts in the last 60 days.

there are x accounts that haven't checked in for the last 60 days. Press
1 to delete these accounts.
