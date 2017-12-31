# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import cherrypy
import wsgigzip

from cross.project import app

host = "0.0.0.0"
port = os.environ.get("PORT", 5000)
def_app = wsgigzip.GzipMiddleware(app)

# --------------------------------------------------------------
cherrypy.config.update({'server.socket_host': host,
                        'server.socket_port': port})
cherrypy.tree.graft(def_app)
cherrypy.engine.start()
cherrypy.engine.block()
#----------------------------------------------------------------

# server = WSGIServer((host, port), def_app, handler_class=WebSocketHandler)
# server.serve_forever()

# https://gist.github.com/dusual/9838932