import os
import boto3
from botocore.exceptions import ClientError
from src.http_response import create_response

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('COURSES_TABLE'))

def get_all_courses():
    try:
        response = table.scan()
        courses = response['Items']
        return create_response(200, courses)
    except ClientError as e:
        return create_response(500, f'Internal server error: {e.response['Error']['Message']}')

def get_courses_by_id(course_ids):
    try:
        courses = table.scan()['Items']
        registered_courses = [course for course in courses if course['id'] in course_ids]
        return {'statusCode': 200, 'body': registered_courses}
    except ClientError as e:
        return create_response(500, f'Internal server error: {e.response['Error']['Message']}')

def get_course_by_id(course_id):
    try:
        response = table.get_item(Key={'id': course_id})
        if 'Item' in response:
             return {'statusCode': 200, 'body': response['Item']}
        return create_response(404, 'Course not found')
    except ClientError as e:
        return create_response(500, f'Internal server error: {e.response['Error']['Message']}')
