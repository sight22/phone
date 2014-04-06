from pyramid.view import view_config

@view_config(route_name='index', renderer='index.jinja2')
def index(request):
    return {}

@view_config(route_name='profile', renderer='profile.jinja2')
def profile(request):
    return {}
