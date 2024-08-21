import json
from src.students import submit_registration

def handler(event, _):
    return submit_registration(event)
       