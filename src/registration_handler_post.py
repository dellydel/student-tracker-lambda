from src.registration import createCourseRegistration 
import json

def handler(event, _):
    body = json.loads(event["body"])
    return  createCourseRegistration(body)
