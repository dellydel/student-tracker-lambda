from botocore.exceptions import ClientError
from src.registration import getRegistrationByEmail 

def handler(event, _):
    query_params = event.get('queryStringParameters', {})
    email = query_params.get('email')
    return  getRegistrationByEmail(email)
