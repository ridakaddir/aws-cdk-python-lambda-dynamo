import json
import os
import uuid
import boto3

dynamodb = boto3.client('dynamodb')

TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    
    
    response = dynamodb.put_item(
        TableName=TABLE_NAME ,
        Item={
             'id': {
                'S': str(uuid.uuid4())
             }
            
        }
    )

    print("PutItem succeeded:")

    return {
        'statusCode': 200,
    }