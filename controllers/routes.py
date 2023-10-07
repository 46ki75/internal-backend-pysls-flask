from flask import Blueprint
from controllers.auth_controller import AuthController
from controllers.bookmark_controller import BookmarkController

# Authentication blueprint setup
auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')
auth_view = AuthController.as_view('auth_controller')
auth_blueprint.add_url_rule('/', view_func=auth_view, methods=['GET', 'POST'])

# Bookmark blueprint setup
auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/bookmark')
bookmark_view = BookmarkController.as_view('bookmark_controller')
auth_blueprint.add_url_rule('/', view_func=bookmark_view, methods=['GET', 'POST'])
