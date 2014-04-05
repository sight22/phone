from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from phone.models import (
    DBSession,
    MyModel,
    )


@view_config(route_name='index', renderer='index.jinja2')
def index(request):
    return {'one': 'one', 'project': 'phone'}
