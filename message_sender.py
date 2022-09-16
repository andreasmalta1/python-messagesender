from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+35679571996",
    from_="+15092608136",
    body="This is a python message"
)

print(message.sid)
