from managers.dynamodb_manager import DynamoDBManager
from datetime import datetime

class BookmarkService:

    @staticmethod
    def get_bookmark():
        db = DynamoDBManager()
        result = db.get_item(PK="BOOKMARK")
        return result
