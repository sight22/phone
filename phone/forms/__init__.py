from wtforms import TextField
from wtforms import validators

from apex.forms import RegisterForm as ApexRegisterForm

class RegisterForm(ApexRegisterForm):
    shelter_name = TextField('Shelter Name', validators=[validators.Required()])
    address_1 = TextField('Address 1', validators=[validators.Required()])
    address_2 = TextField('Address 2')
    city = TextField('City', validators=[validators.Required()])
    state = TextField('State', validators=[validators.Required()])
    zip = TextField('Zip', validators=[validators.Required()])

    def after_signup(self, user, **kwargs):
        pass
