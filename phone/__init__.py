from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')

    """
    Twillio section
    """
    config.add_route('twillio_index', '/twillio/')
    config.add_route('twillio_mailbox', '/twillio/mailbox')
    config.add_route('twillio_mailbox_admin', '/twillio/mailbox_admin')
    # listen to active, or saved
    config.add_route('twillio_mailbox_admin_listen',
        '/twillio/mailbox_admin_listen')
    config.add_route('twillio_mailbox_admin_change_greeting',
        '/twillio/mailbox_admin_change_greeting')
    config.add_route('twillio_create_mailbox', '/twillio/create_mailbox')

    config.scan()
    return config.make_wsgi_app()
