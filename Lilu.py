
from flask import Blueprint, Response

liluMod = Blueprint('Lilu', __name__)



@liluMod.route('/')
def home():
    return 'Li\'lu home'


@liluMod.route("/Your_mom_is_a_river")
def your_mom_is_a_river():
    def generate():
        with open("Lilu/momisriver.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")
    
@liluMod.route("/Say_that_to_my_face_you_fucker")
def say_that_to_my_face_you_fucker():
    def generate():
        with open("Lilu/saythattomyface.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@liluMod.route("/We_are_going_to_decapitate_them")
def We_are_going_to_decapitate_them():
    def generate():
        with open("Lilu/weregoingtodecapitatethem.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@liluMod.route("/Who_named_you")
def Who_named_you():
    def generate():
        with open("Lilu/whonamedu.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")