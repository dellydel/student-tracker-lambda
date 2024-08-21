from src.http_response import create_response
from src.courses import get_course_by_id, get_all_courses

def handler(event, context):
    query_params = event.get('queryStringParameters')
    if query_params and 'courseId' in query_params:
        course_id = query_params['courseId']
        return get_course_by_id(course_id)
    return get_all_courses()

