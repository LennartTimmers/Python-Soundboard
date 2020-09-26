
from flask import Blueprint, Response


pmisMod = Blueprint('Pmis', __name__)


@pmisMod.route('/')
def home():
    return 'P\'mis/D\'ahc home'

@pmisMod.route("/Tell_him_lady_Ear")
def Tell_him_lady_ear():
    def generate():
        with open("Pmis/tellhimladyear.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@pmisMod.route("/Dive_bomb_her")
def Dive_bomb_her():
    def generate():
        with open("Pmis/divebombher.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@pmisMod.route("/I_will_call_you_whatever_I_please")
def I_will_call_you_whatever_I_please():
    def generate():
        with open("Pmis/iwillcallyouwhateveriplease.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@pmisMod.route("/Pmis_feels_real_good")
def Pmis_feels_real_good():
    def generate():
        with open("Pmis/pmisfeelsrealgood.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@pmisMod.route("/Pmis_is_no_longer_the_weakest")
def Pmis_is_no_longer_the_weakest():
    def generate():
        with open("Pmis/pmisisnolongertheweakestone.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@pmisMod.route("/Sorry_about_the_kamikaze_owl")
def Sorry_about_the_kamikaze_owl():
    def generate():
        with open("Pmis/sorryaboutthekamikazeowl.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@pmisMod.route("/We_will_just_take_the_child")
def We_will_just_take_the_child():
    def generate():
        with open("Pmis/welljusttakethechild.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@pmisMod.route("/You_know_how_I_can_get_more_power")
def You_know_how_I_can_get_more_power():
    def generate():
        with open("Pmis/youknowhowicangetmorepower.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@pmisMod.route("/You_will_answer_for_your_crimes")
def You_will_answer_for_your_crimes():
    def generate():
        with open("Pmis/youwillanswerforyourcrimes.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

    