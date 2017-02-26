import requests
import os

url = os.environ['MAILGUN_URL']
key = os.environ['MAILGUN_KEY']
from_address = os.environ['MAILGUN_FROM']

def sendMessage(emailAddress, message):
    data = {"from": from_address,
            "to": emailAddress,
            "subject": "This week in Reddit",
            "text": message
            }
    auth = ("api", key)
    return requests.post(url, auth=auth, data=data)
