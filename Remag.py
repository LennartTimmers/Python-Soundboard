
from flask import Blueprint, Response


remagMod = Blueprint('Remag', __name__)


@remagMod.route('/')
def home():
    return 'Remag home'

@remagMod.route("/Good_job_pmis")
def Good_job_pmis():
    def generate():
        with open("Remag/goodjobpmis.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@remagMod.route("/Move_the_fuck_away")
def Move_the_fuck_away():
    def generate():
        with open("Remag/movethefuckaway.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@remagMod.route("/We_will_all_be_with_god_soon")
def We_will_all_be_with_god_soon():
    def generate():
        with open("Remag/wellbewithgodsoon.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@remagMod.route("/Hashbrown_looking_ass")
def Hashbrown_looking_ass():
    def generate():
        with open("Remag/hashbrownlookingass.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@remagMod.route("/I_have_seen_god")
def I_have_seen_god():
    def generate():
        with open("Remag/iveseengod.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@remagMod.route("/Uh_oh_stinky")
def Uh_oh_stinky():
    def generate():
        with open("Remag/uhohstinky.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@remagMod.route("/What_a_bitch")
def What_a_bitch():
    def generate():
        with open("Remag/whatabitch.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@remagMod.route("/Why_is_that_small_bird_talking")
def Why_is_that_small_bird_talking():
    def generate():
        with open("Remag/whybirdtalks.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@remagMod.route("/Why_is_that_bucket_of_water_talking")
def Why_is_that_bucket_of_water_talking():
    def generate():
        with open("Remag/whyisbuckettalking.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")