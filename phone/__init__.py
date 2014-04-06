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
    config.add_route('profile', '/profile')

    """
    Twilio section
    """
    config.add_route('twilio_index', '/twilio/')
    config.add_route('twilio_process_input',
        '/twilio/process_input/:star/:numeric')
    config.add_route('twilio_mailbox', '/twilio/mailbox')
    config.add_route('twilio_mailbox_admin', '/twilio/mailbox_admin')
    # listen to active, or saved
    config.add_route('twilio_mailbox_admin_listen',
        '/twilio/mailbox_admin_listen')
    config.add_route('twilio_mailbox_admin_change_greeting',
        '/twilio/mailbox_admin_change_greeting')
    config.add_route('twilio_create_mailbox', '/twilio/create_mailbox')

    config.scan()

    config.include('apex', route_prefix='/auth')
    return config.make_wsgi_app()
