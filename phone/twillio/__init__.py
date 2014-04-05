from pyramid.response import Response
from pyramid.view import view_config

from twilio import twiml

@view_config(route_name='twillio_index')
def index(request):
    response = twiml.Response()
    response.enqueue("Queue Demo")
    return Response(str(response))

@view_config(route_name='twillio_mailbox')
def mailbox(request):
    response = twiml.Response()
    response.enqueue("Queue Demo")
    return Response(str(response))

@view_config(route_name='twillio_mailbox_admin')
def mailbox_admin(request):
    response = twiml.Response()
    response.enqueue("Queue Demo")
    return Response(str(response))

@view_config(route_name='twillio_mailbox_admin_listen')
def listen(request):
    response = twiml.Response()
    response.enqueue("Queue Demo")
    return Response(str(response))

@view_config(route_name='twillio_mailbox_admin_change_greeting')
def change_greeting(request):
    response = twiml.Response()
    response.enqueue("Queue Demo")
    return Response(str(response))

@view_config(route_name='twillio_create_mailbox')
def create_mailbox(request):
    response = twiml.Response()
    response.enqueue("Queue Demo")
    return Response(str(response))
