import boto3
from botocore.exceptions import ClientError
from src.http_response import create_response

s3_client = boto3.client('s3')

def get_course_materials(topic):
    try:
        objects = list_all_materials(topic)
        files = generate_presigned_urls(objects)
        return create_response(200, files)
    except Exception as e:
        error_message = e.response['Error']['Message']
        return create_response(500, f'Internal server error: {error_message}')
    
def list_all_materials(topic):
    bucket_name = "nextbyte-course-materials"
    prefix = topic
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    except ClientError as e:
        error_message = e.response['Error']['Message']
        return create_response(500, f'Internal server error: {error_message}')

    if 'IsTruncated' in response and response['IsTruncated']:
        return create_response(500, "Course Materials List truncated")

    objects = [obj for obj in response['Contents'] if not obj['Key'].endswith('/')]
    return objects

def generate_presigned_urls(objects):
    bucket_name = "nextbyte-course-materials"
    files = []
    for obj in objects:
        try:
             url = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name, 'Key': obj['key']},
                                                    ExpiresIn=1800)
             files.append({'name': obj['Key'], 'url': url})
        except ClientError as e:
            error_message = e.response['Error']['Message']
        return create_response(500, f'Internal server error: {error_message}')
    return files