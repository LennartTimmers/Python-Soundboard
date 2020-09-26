
from flask import Blueprint, Response

audioHandler = Blueprint('audioHandler', __name__)



@audioHandler.route('/')
def home():
    return 'audioHandler home'

#the route so in this case localhost:5000/Audio/Example
@audioHandler.route("/Example")
def Example():
    def generate():
        with open("Audio/Example.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")
    
