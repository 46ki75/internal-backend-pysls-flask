from flask import Blueprint, jsonify

hello_controller = Blueprint('hello_controller', __name__)

@hello_controller.route("/hello")
def hello():
    return jsonify(message='Hello from path!')
