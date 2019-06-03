import sys
from flask import Flask
from controllers import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)
app.config['SECRET_KEY'] = "09d3a1efda7a5b3d270e0f6ad986d7e2"

if __name__=="__main__":
	app.run(port=8080, host="0.0.0.0")
