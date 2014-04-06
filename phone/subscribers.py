from pyramid.events import subscriber
from pyramid.events import BeforeRender
from pyramid.threadlocal import get_current_request

#@subscriber(BeforeRender)
def is_profile_setup(event):
    request = event.get('request')
    if request is None:
        request = get_current_request()

    if request.user:
      print request.user
