from src.http_response import create_response
from src.courses import get_courses_by_id

def handler(event, _):
    course_ids = event['courseIds']
    if not course_ids:
        return create_response(200, [])
    return get_courses_by_id(course_ids)