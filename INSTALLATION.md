If you want to run your own version of the Twimlet server, follow these 
instructions. If you want to have us host the Twimlet just go to 
http://phone.cd34.com/

Installation Instructions
=========================

  virtualenv /var/www/site
  cd /var/www/site
  source bin/activate
  easy_install https://github.com/Qwait/python-temboo/tarball/master
  git clone https://github.com/Qwait/phone
  cd phone
  python setup.py develop
  pserver --reload development.ini

  Visit http://yourhostname.com:6543/

  https://www.temboo.com/account/applications
  Create a new App, choose an Application name. Copy the Application Name
  and key into phone.cfg.
