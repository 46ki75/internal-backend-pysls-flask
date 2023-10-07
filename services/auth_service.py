from models.user_model import UserModel
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class AuthService:
    """
    A service class dedicated to handle authentication related operations.
    """

    @staticmethod
    def get_login_instruction():
        """
        Provides a descriptive message for the login page.
        
        This method returns a message that instructs users to use 
        the POST method for login authentication.
        
        Returns:
        - str: A message describing the login authentication process.
        """
        return 'This is the pass for login authentication. Use the POST method for login authentication.'
    
    @staticmethod
    def verify(name, password):
        user = UserModel()
        return user.verify(name=name,password=password)
        
