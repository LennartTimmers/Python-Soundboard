from flask import Flask, url_for
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

app.debug = True


soundboardName = "Python"


#method that retrieves all available routes that the api has
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
from AudioHandler import audioHandler


#register blueprints in the app. URL_prefix is the path that is used in the url so in this case: localhost:5000/Audio
app.register_blueprint(audioHandler, url_prefix='/Audio')





if __name__ == '__main__':
    app.run(host='0.0.0.0')
