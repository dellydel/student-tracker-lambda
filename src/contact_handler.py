import json 
from src.contact import process_contact_request

def handler(event, _):
    body = json.loads(event["body"])
    name = body.get("name")
    email = body.get("email")
    message = body.get("message")
    return process_contact_request(name, email, message)