from flask.views import MethodView
from flask import jsonify, request
from services.auth_service import AuthService

class AuthController(MethodView):
    """
    Controller to handle authentication related endpoints.
    
    Methods:
    - GET: Returns a login page.
    - POST: Handles the user login process based on provided credentials.
    """

    def get(self):
        """
        Handle GET request for the authentication endpoint.
        
        Returns:
        JsonResponse containing a message indicating it's the login page.
        """
        message = AuthService.get_login_instruction()
        return jsonify(message=message)

    def post(self):
        """
        Handle POST request for the authentication endpoint.
        
        This method expects a JSON payload with 'username' and 'password'.
        
        Returns:
        JsonResponse containing a message with the logged in username 
        or an error message in case of failure.
        """
        data = request.get_json()
        return jsonify(AuthService.verify(name = data.get('name'),password = data.get('password')))
