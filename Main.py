from flask import Flask, url_for
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

app.debug = True


soundboardName = "Broken Bonds"



def list_routes():
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        output.append(url)
    routes = ""
    for line in sorted(output):
        print (line)
        routes += line + '\n' 
    return sorted(output)

@app.route('/')
def hello_world():

    return 'Welcome to the '+ soundboardName + ' soundboard API! '

@app.route('/routes')
def availableRoutes():
    return json.dumps(list_routes())


#Load modules 
from Remag import remagMod
from ear import earMod
from Lilu import liluMod
from Brian import brianMod
from Pmis import pmisMod
from Hashbrown import hashbrownMod

#register blueprints in the app
app.register_blueprint(remagMod, url_prefix='/remag')
app.register_blueprint(earMod, url_prefix='/ear')
app.register_blueprint(liluMod, url_prefix='/lilu')
app.register_blueprint(brianMod, url_prefix='/brian')
app.register_blueprint(pmisMod, url_prefix='/pmis')
app.register_blueprint(hashbrownMod, url_prefix='/hashbrown')




if __name__ == '__main__':
    app.run(host='0.0.0.0')
