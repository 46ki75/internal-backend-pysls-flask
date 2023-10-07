from flask import Blueprint
from controllers.auth_controller import AuthController

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')
auth_view = AuthController.as_view('auth_controller')
auth_blueprint.add_url_rule('/', view_func=auth_view, methods=['GET', 'POST'])
