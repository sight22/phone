import webhelpers.constants as constants

from wtforms import IntegerField
from wtforms import TextField
from wtforms import SelectField
from wtforms import validators

from phone.models import DBSession
from phone.models import Shelter

from apex.forms import RegisterForm as ApexRegisterForm

class RegisterForm(ApexRegisterForm):
    shelter_name = TextField('Shelter Name', validators=[validators.Required()])
    address_1 = TextField('Address 1', validators=[validators.Required()])
    address_2 = TextField('Address 2')
    city = TextField('City', validators=[validators.Required()])
    state = SelectField('State', choices=constants.us_states(),
      validators=[validators.Required()])
    zip = IntegerField('Zip', validators=[validators.Required()])

    def after_signup(self, user, **kwargs):
        profile = Shelter(auth_id=user.id)
        profile.name = self.shelter_name.data
        profile.address_1 = self.address_1.data
        if self.address_2:
            profile.address_2 = self.address_2.data
        profile.city = self.city.data
        profile.state = self.state.data
        profile.zip = self.zip.data

        DBSession.add(profile)
        DBSession.flush()

