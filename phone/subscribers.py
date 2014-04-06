from pyramid.events import subscriber
from pyramid.events import ContextFound
from pyramid.httpexceptions import HTTPFound
from pyramid.threadlocal import get_current_request

@subscriber(ContextFound)
def is_profile_setup(event):
    request = event.request
    if request is None:
        request = get_current_request()

    if request.user:
      profile = request.user.get_profile(request)

      if profile is None and request.matched_route.name != 'profile':
         raise HTTPFound(location=request.route_url('profile')) 
