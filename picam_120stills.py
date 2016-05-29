#!/usr/bin/env python
# Chrisnel


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    start = time.time()
    camera.capture_sequence((
        '\home\pi\picam\image%03d.jpg' % i
        for i in range(120)
        ), use_video_port=True)
    print('Captured 120 images at %.2ffps' % (120 / (time.time() - start)))
    camera.stop_preview()


