from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from apex.lib.db import merge_session_with_post

from phone.forms import ProfileForm

from phone.models import DBSession
from phone.models import Shelter

@view_config(route_name='index', renderer='index.jinja2')
def index(request):
    return {}

@view_config(route_name='profile', renderer='profile.jinja2')
def profile(request):
    record = DBSession.query(Shelter).filter(Shelter.auth_id==request.user.id).first()
    if record is None:
      record = Shelter()

    form = ProfileForm(request.POST, obj=record)

    if request.method == 'POST' and form.validate():
        record = merge_session_with_post(record, request.POST.items())
        record.auth_id = request.user.id
        if record.id:
            DBSession.merge(record)
        else:
            DBSession.add(record)
        DBSession.flush()
        raise HTTPFound(location=request.route_url('index'))
    return {'form': form}

@view_config(route_name='connect', renderer='connect.jinja2')
def connect(request):
    return {}
