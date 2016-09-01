
from flask import Response
import time
from app.sessionManager.tools import check_permission
from app import app, video

if app.config['WEB_CAMERA_TYPE'] == 'usb_camera':
    from app.camera.web_camera import Camera
    camera = Camera()
elif app.config['WEB_CAMERA_TYPE'] == 'pi_camera':
    from app.camera.pi_camera import Camera
    camera = Camera()
else:
    print 'Camera type not supported'
    camera = None
    #TODO:ADD FAKE CAMERA WITH FIXED IMAGE




def gen(camera):
    """Video streaming generator function."""
    while True:
        time.sleep(0.2)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




@video.route('/video_feed')
@check_permission
def video_feed():
    global camera
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')