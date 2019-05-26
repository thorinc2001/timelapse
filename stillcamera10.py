from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(10):
    sleep(5)
    camera.capture('/home/pi/Pictures/image%s.jpg' % i)
camera.stop_preview()
