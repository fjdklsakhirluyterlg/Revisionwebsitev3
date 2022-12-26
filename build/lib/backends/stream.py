from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
import cv2

stream = Blueprint("stream", __name__)

@stream.route("/stream")
def stream():
    video = cv2.VideoCapture(0)
    def generator(webcam):
        while True:
            success, image = video.read()
            if success:
                ret, jpeg = cv2.imencode('.jpg', image)
                frame = jpeg.tobytes()
                yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
    return Response(generator(video),mimetype='multipart/x-mixed-replace; boundary=frame')