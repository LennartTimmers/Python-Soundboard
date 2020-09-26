
from flask import Blueprint, Response


brianMod = Blueprint('Brian', __name__)


@brianMod.route('/')
def home():
    return 'Brian home'


@brianMod.route("/Hey_so_you_know_babylon")
def Hey_so_you_know_babylon():
    def generate():
        with open("Brian/heysoyouknowbabylon.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")
    
@brianMod.route("/I_love_him")
def I_love_him():
    def generate():
        with open("Brian/ilovehim.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@brianMod.route("/I_love_Babylon")
def I_love_Babylon():
    def generate():
        with open("Brian/ilovebabylon.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@brianMod.route("/Oh_my_love_where_have_you_gone")
def Oh_my_love_where_have_you_gone():
    def generate():
        with open("Brian/Ohmylovewherehaveyougone.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@brianMod.route("/I_live_only_for_you_babylon")
def I_live_only_for_you_babylon():
    def generate():
        with open("Brian/iliveonlyforyoubabylon.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@brianMod.route("/What_are_you_looking_at_pmis")
def What_are_you_looking_at_pmis():
    def generate():
        with open("Brian/whatareyoulookingatpmis.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")