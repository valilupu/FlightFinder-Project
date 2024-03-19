from twilio.rest import Client

TWILIO_VERIFIED_NUMBER = "+40 744 775 351"
TWILIO_VIRTUAL_NUMBER = "+12708125911"
TWILIO_SID = "AC056c4a20a48a3a3d26d8095dff4d086f"
TWILIO_AUTH_TOKEN = "74b76608b216f21dd2ba372002928810"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
