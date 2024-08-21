from src.students import submit_registration

def handler(event, _):
    body = event['body']
    return submit_registration(body)
       