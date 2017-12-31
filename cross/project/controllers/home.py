# -*- coding: UTF-8 -*-
import bottle
from bottle import view, request, redirect
from .mail import send_mail


@bottle.route('/')
@view('index')
def index():
    return dict(csf="resources/css/styles.css")


@bottle.route('/send', method='POST')
def do_admin():
    user_name = request.forms.get('name')
    user_text = request.forms.get('text')

    send_mail('nsitala@gmail.com', 'nsitala@gmail.com', user_name, user_text)

    redirect('/')




