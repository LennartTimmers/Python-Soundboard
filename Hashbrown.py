
from flask import Blueprint, Response


hashbrownMod = Blueprint('Hashbrown', __name__)


@hashbrownMod.route('/')
def home():
    return 'Hashbrown home'

@hashbrownMod.route("/I_can_cook_hashbrowns_pretty_well")
def I_can_cook_hashbrowns_pretty_well():
    def generate():
        with open("Hashbrown/icancookhashbrownsprettywel.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@hashbrownMod.route("/Who_named_u")
def Who_named_u():
    def generate():
        with open("Hashbrown/whonameduhb.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")