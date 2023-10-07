from managers.dynamodb_manager import DynamoDBManager
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class UserModel:
    
    def __init__(self):
        db = DynamoDBManager()
        user = db.get_item(PK="USER", SK="PROFILE")
        print(user)
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
        return bcrypt.check_password_hash(self.password,password)

    