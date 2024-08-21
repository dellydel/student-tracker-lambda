from botocore.exceptions import ClientError
from src.materials import get_course_materials

def handler(event, _):
    query_params = event.get('queryStringParameters', {})
    topic = query_params.get('topic')
    return get_course_materials(topic)