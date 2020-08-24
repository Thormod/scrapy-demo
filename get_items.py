import json
import decimal
import boto3
from boto3.dynamodb.conditions import Key, Key
from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy',
    region_name='us-east-1',
    endpoint_url='http://localhost:8042'
)

table = dynamodb.Table('News')
response = table.scan()
items = response['Items']

with open(f"response/news.json", "w+") as file1:
    file1.write(json.dumps(response))
    data = []
