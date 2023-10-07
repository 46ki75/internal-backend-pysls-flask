import boto3

class DynamoDBModel:
    def __init__(self, table_name='internal', region_name='ap-northeast-1'):
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)
        self.table = self.dynamodb.Table(table_name)

    def get_item(self, key):
        response = self.table.get_item(Key=key)
        return response.get('Item')

    def put_item(self, item):
        self.table.put_item(Item=item)

