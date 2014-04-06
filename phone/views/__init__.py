from pyramid.view import view_config

from phone.forms import ProfileForm

@view_config(route_name='index', renderer='index.jinja2')
def index(request):
    return {}

@view_config(route_name='profile', renderer='profile.jinja2')
def profile(request):
    form = ProfileForm(request.POST)

    if request.method == 'POST' and form.validate():
        print request.POST
    return {'form': form}
