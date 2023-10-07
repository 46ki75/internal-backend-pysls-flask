import boto3
import os
import json

class DynamoDBManager:
    """
    A class to manage DynamoDB operations.

    Attributes:
        dynamodb: An instance of the DynamoDB resource.
        table: An instance of the DynamoDB table.
    """

    def __init__(self, table_name='internal', region_name='ap-northeast-1'):
        """
        Initializes the DynamoDBManager with the given table name and region.

        Args:
            table_name (str): The name of the DynamoDB table. Defaults to 'internal'.
            region_name (str): The AWS region name. Defaults to 'ap-northeast-1'.
        """
        aws_access_key_id = os.environ.get('SLS_AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.environ.get('SLS_AWS_SECRET_ACCESS_KEY')
        boto3_session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        self.dynamodb = boto3_session.resource('dynamodb', region_name=region_name)   
        self.table = self.dynamodb.Table(table_name)

    def get_item(self, PK=None, SK=None):
        """
        Retrieves an item or items from the DynamoDB table.

        Args:
            PK (str, optional): The partition key value.
            SK (str, optional): The sort key value.

        Returns:
            dict or list: The retrieved item(s).

        Raises:
            ValueError: If neither PK nor SK is provided.

        Example:
            ```python
            db = DynamoDBManager()
            item = db.get_item(PK='BOOKMARK', SK='2023-10-05T16:36:12.871Z')
            ```
        """
        if PK and SK:
            key = {
                'PK': PK,
                'SK': SK
            }
            response = self.table.get_item(Key=key)
            return response.get('Item')
        elif PK: 
            response = self.table.query(
                KeyConditionExpression=boto3.dynamodb.conditions.Key('PK').eq(PK)
            )
            return response.get('Items')
        else:
            raise ValueError("At least PK must be provided.")

    def get_all_items(self):
        """
        Retrieves all items from the DynamoDB table using a scan operation.

        Returns:
            list: A list of all items.
            
        Example:
            ```python
            db = DynamoDBManager()
            item = db.get_all_items()
            ```

        Warning:
            This method uses the scan operation, which can be inefficient and costly on large tables.
        """
        response = self.table.scan()
        return response.get('Items')

    def put_item(self, PK, SK, attributes):
        """
        Inserts or updates an item in the DynamoDB table.

        Args:
            PK (str): The partition key value.
            SK (str): The sort key value.
            attributes (dict): Additional attributes to set or update for the item.

        Returns:
            dict: The inserted or updated item.

        Example:
            ```python
            db = DynamoDBManager()
            item_data = {
                'title': 'Awesome title',
                'attribute1': 'value1',
                'attribute2': 'value2'
            }
            item = db.put_item(PK='EXAMPLE', SK='2023-10-07T17:36:38.521442', attributes=item_data)
            ```
        """
        item = {
            'PK': PK,
            'SK': SK
        }
        item.update(attributes)
        self.table.put_item(Item=item)
        return item

    def delete_item(self, PK, SK):
        """
        Deletes an item from the DynamoDB table.

        Args:
            PK (str): The partition key value.
            SK (str): The sort key value.

        Returns:
            dict: The attributes of the deleted item.

        Example:
            ```python
            db = DynamoDBManager()
            deleted_item = db.delete_item(PK='BOOKMARK', SK='2023-10-05T16:36:12.871Z')
            ```
        """
        key = {
            'PK': PK,
            'SK': SK
        }
        response = self.table.delete_item(Key=key, ReturnValues='ALL_OLD')
        return response.get('Attributes', {})
