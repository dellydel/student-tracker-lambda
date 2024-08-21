import os
import boto3
from boto3.dynamodb.types import TypeDeserializer
from botocore.exceptions import ClientError
from src.http_response import create_response

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
table = dynamodb.Table(os.environ.get('STUDENTS_TABLE'))

def submit_registration(body):
    try:
        table.put_item(Item=body)
        return create_response(201, "Your submission was successful.")
    except ClientError as e:
      error_message = e.response['Error']['Message']
      return create_response(500, f'Internal server error: {error_message}')

def get_student_by_id(student_id):
    try:
        response = table.get_item(Key={'id': student_id})
        if 'Item' in response:
            return create_response(200, response['Item'])
        else:
            return create_response(404, "Student not found")
    except ClientError as e:
      error_message = e.response['Error']['Message']
      return create_response(500, f'Internal server error: {error_message}')

def get_student_by_email(email):
    try:
        response = client.query(
            TableName=os.environ.get('STUDENTS_TABLE'),
            IndexName='EmailIndex',
            KeyConditionExpression='email = :email',
            ExpressionAttributeValues={':email': {'S': email}}
        )
        deserializer = TypeDeserializer()
        students = [deserializer.deserialize({'M': item}) for item in response.get('Items', [])]
        return create_response(200, students[0] if students else [])
    except ClientError as e:
      error_message = e.response['Error']['Message']
      return create_response(500, f'Internal server error: {error_message}')

