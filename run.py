#!/usr/bin/python

from app import app,socketio
from  config import DEBUG
from config import PORT

socketio.run(app, "0.0.0.0", port=8000,debug=DEBUG)
