from http_response import create_response
from src.students import get_student_by_id, get_student_by_email

def handler(event, _):
    path_params = event.get('pathParameters')
    if path_params and 'studentId' in path_params:
        student_id = path_params['studentId']
        return get_student_by_id(student_id)
    elif event.get('queryStringParameters') and 'email' in event['queryStringParameters']:
        email = event['queryStringParameters']['email']
        return get_student_by_email(email)
    else:
        return create_response(400, "Invalid request")
