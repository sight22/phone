import ConfigParser
import os

from temboo.core.session import TembooSession
from temboo.Library.Google.Geocoding import GeocodeByAddress
from temboo.Library.Twilio.AvailablePhoneNumbers import LocalList
from temboo.Library.Twilio.IncomingPhoneNumbers import AddPhoneNumber
from temboo.Library.SendGrid.WebAPI.Mail import SendMail

def get_phones(addr1, city, state, zip):
    config = ConfigParser.ConfigParser()
    config.readfp(open(os.path.join('/', os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.join(os.path.abspath(__file__))))), 'phone.cfg')))

    session = TembooSession('cd34', config.get('temboo', 'APP_KEY_NAME'),
        config.get('temboo', 'APP_KEY_VALUE'))

    address = '{addr} {city}, {state} {zip}'.format(
        addr=addr1, city=city, state=state, zip=zip)

    geocodeByAddressChoreo = GeocodeByAddress(session)
    geocodeByAddressInputs = geocodeByAddressChoreo.new_input_set()
    geocodeByAddressInputs.set_Address(address)
    geocodeByAddressResults = geocodeByAddressChoreo \
        .execute_with_results(geocodeByAddressInputs)
    latitude = geocodeByAddressResults.get_Latitude()
    longitude = geocodeByAddressResults.get_Longitude()

    localListChoreo = LocalList(session)
    localListInputs = localListChoreo.new_input_set()
    localListInputs.set_AuthToken(config.get('twilio', 'auth_token'))
    localListInputs.set_AccountSID(config.get('twilio', 'account_sid'))
    localListInputs.set_Latitude(latitude)
    localListInputs.set_Longitude(longitude)
    localListInputs.set_Distance(10)
    localListInputs.set_PageSize(10)

    TwilioResults = localListChoreo.execute_with_results(localListInputs)
    numbers = TwilioResults.getJSONFromString(TwilioResults.get_Response())

    return numbers['available_phone_numbers']

def buy_number(account_sid, number):
    config = ConfigParser.ConfigParser()
    config.readfp(open(os.path.join('/', os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.join(os.path.abspath(__file__))))), 'phone.cfg')))

    session = TembooSession('cd34', config.get('temboo', 'APP_KEY_NAME'),
        config.get('temboo', 'APP_KEY_VALUE'))

    addPhoneNumberChoreo = AddPhoneNumber(session)
    addPhoneNumberInputs = addPhoneNumberChoreo.new_input_set()

    addPhoneNumberInputs.set_AuthToken(config.get('twilio', 'auth_token'))
    addPhoneNumberInputs.set_AccountSID(account_sid)

    addPhoneNumberResults = addPhoneNumberChoreo.execute_with_results(addPhoneNumberInputs)

    #print addPhoneNumberResults

    return addPhoneNumberResults

def send_mail(subject, data, to_address, from_address=None):
    config = ConfigParser.ConfigParser()
    config.readfp(open(os.path.join('/', os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.join(os.path.abspath(__file__))))), 'phone.cfg')))

    session = TembooSession('cd34', config.get('temboo', 'APP_KEY_NAME'),
        config.get('temboo', 'APP_KEY_VALUE'))

    sendMailChoreo = SendMail(session)
    sendMailInputs = sendMailChoreo.new_input_set()

    if from_address is None:
        from_address = config.get('sendgrid', 'default_from')

    sendMailInputs.set_APIUser(config.get('sendgrid', 'api_user'))
    sendMailInputs.set_APIKey(config.get('sendgrid', 'api_key'))
    sendMailInputs.set_Subject(subject)
    sendMailInputs.set_To(to_address)
    sendMailInputs.set_From(from_address)
    sendMailInputs.set_Text(data)
