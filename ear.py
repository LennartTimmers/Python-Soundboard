
from flask import Blueprint, Response


earMod = Blueprint('Ear', __name__)


@earMod.route('/')
def home():
    return 'E\'ar home'


@earMod.route("/I_can_fit_in_buckets")
def I_can_fit_in_buckets():
    def generate():
        with open("Ear/icanfitinbuckets.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")
    
@earMod.route("/Sounds_like_he_is_trying_to_take_your_man")
def Sounds_like_he_is_trying_to_take_your_man():
    def generate():
        with open("Ear/soundslikehestryingtotakeyourman.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")