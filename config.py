import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

APPLICATION_ROOT="/labs/dummy"
PORT = 8000

CSRF_ENABLED = True
SECRET_KEY = 'SECRET_PASSWORD_HERE'

SESSION_COOKIE_NAME = 'dummy_cookie'
SESSION_COOKIE_PATH = '/'

WEBLAB_USERNAME = 'weblab_instance_name'
WEBLAB_PASSWORD = 'weblab_password'

#Set True for ena
WEB_CAMERA = True

#Select type of camera
WEB_CAMERA_TYPE = "usb_camera"
#WEB_CAMERA_TYPE = "pi_camera"

#Set to True for running computer vision algorithm
AV = True
#algorithm = "none"
algorithm = "face_detect"