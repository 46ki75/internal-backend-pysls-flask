from flask import Flask, jsonify, make_response
from controllers.routes import auth_blueprint  

app = Flask(__name__)
app.register_blueprint(auth_blueprint)

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)