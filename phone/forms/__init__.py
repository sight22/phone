import webhelpers.constants as constants

from wtforms import IntegerField
from wtforms import TextField
from wtforms import SelectField
from wtforms import validators

from phone.models import DBSession
from phone.models import Shelter

from apex.forms import ExtendedForm

class ProfileForm(ExtendedForm):
    name = TextField('Shelter Name', validators=[validators.Required()])
    address_1 = TextField('Address 1', validators=[validators.Required()])
    address_2 = TextField('Address 2')
    city = TextField('City', validators=[validators.Required()])
    state = SelectField('State', choices=constants.us_states(),
        validators=[validators.Required()])
    zip = IntegerField('Zip', validators=[validators.Required()])
    paypal_email = TextField('Paypal Email',
        validators=[validators.Required(), validators.email()])
