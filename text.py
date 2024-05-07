import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone = os.environ['TWILIO_PHONE_NUMBER']
personal_phone = os.environ['PERSONAL_PHONE_NUMBER']
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=twilio_phone,
  body='Hello world2',
  to=personal_phone
)

print(message.sid)