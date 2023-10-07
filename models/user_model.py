from managers.dynamodb_manager import DynamoDBManager
from flask_bcrypt import Bcrypt
import jwt
import datetime

import os

bcrypt = Bcrypt()
SECRET_KEY = "YOUR_SECRET_KEY"

class UserModel:
    
    def __init__(self):
        db = DynamoDBManager()
        user = db.get_item(PK="USER", SK="PROFILE")
        self.name = user['name']
        self.password = user['password']

        
    def verify(self,name,password):
        """
        Verifies the provided user name and password against data in UserModel instance.
        
        Args:
            name (str): The user name to verify.
            password (str): The password to verify.
        
        Returns:
            bool: True if the user name and password match the data in DynamoDB, False otherwise.
        
        Usage:
            ```python
            user = UserModel()
            user.verify(name="blanc",password="myPass)
            ```
            
        Return:
            bool True/False
        """
        
        # Return False if the user does not exist or if the user name does not match
        if self.name != name:
            return False
        
        # Verify the bcrypt-hashed password
        if bcrypt.check_password_hash(self.password,password):
            return self.generate_jwt()
        return False

    
    def generate_jwt(self):
        """
        Generates a JSON Web Token for the user.

        Returns:
            dict: A dictionary containing the generated JWT under the key "token".

        Example:
            ```python
            user = UserModel()
            jwt_data = user.generate_jwt()
            print(jwt_data["token"])
            ```

        Output:
            {
                "token": "YOUR_JWT_TOKEN_HERE"
            }
        """
        payload = {
            "name": self.name,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1) 
        }
        token = jwt.encode(payload, os.environ.get('JWT_SECRET_KEY'), algorithm="HS256")
        return {"token":token}