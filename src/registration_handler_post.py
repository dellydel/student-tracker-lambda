from src.registration import create_course_registration 

def handler(event, _):
    return  create_course_registration(event)
