# set async_mode to 'threading', 'eventlet', 'gevent' or 'gevent_uwsgi' to
# force a mode else, the best mode is selected automatically from what's
# installed
async_mode = None

import os

from django.http import HttpResponse
import socketio

basedir = os.path.dirname(os.path.realpath(__file__))

# 
# https://stackoverflow.com/questions/57579110/how-to-fix-access-control-allow-origin-error-in-a-python-socket-io-server
sio = socketio.Server(async_mode=async_mode, cors_allowed_origins='*')
# sio = socketio.Server(async_mode=async_mode)
thread = None

from .db_helper import get_or_create_note, update_note

def index(request):
    return HttpResponse("Hello, world. You're at the notes index.")

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    print('background_thread')
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my_response', {'data': 'Server generated event'},
                 namespace='/test')

@sio.event
def disconnect_request(sid):
    print('disconnect_request')
    sio.disconnect(sid)

@sio.event
def connect(sid, environ):
    print('Połączono z serwerem')
    sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)

@sio.event
def disconnect(sid):
    print('Client disconnected')

@sio.event
def save_document(sid, data):
    update_note(data['documentId'], data['data'])
    sio.emit('my_response_save_document', 'ala ma kota', room=data['documentId'] )

@sio.event 
def get_document(sid, document_id):
    # 1. wejsc do pooju o id dokumentu
    sio.enter_room(sid, document_id)
    # 2. pobrać dane dokuemntu {'_id':24ZnakowyHex, 'data':'String z danymi z edytora'}
    data = get_or_create_note(document_id)
    #3. wysłąć na front do zdarzenia 'load_document'
    sio.emit('load_document', data=data['data'], room=document_id)

@sio.event
def send_changes(sid, data):    
    update_note(data['documentId'], data['delta'])
    sio.emit('receive-changes',data['delta'], room=data['documentId'], skip_sid=sid) #dla JS zdarzenie

@sio.event
def leave(sid, room_name):
    sio.leave_room(sid, room_name)
    sio.emit('my_response', {'data': 'Left room: ' + room_name},
             room=sid)
