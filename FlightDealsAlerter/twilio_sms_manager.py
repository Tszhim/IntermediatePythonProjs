from twilio.rest import Client

class TwilioSMSManager:
    
    # Instantiating relevant information to make TWilio API call.
    def __init__(self):
        self.twilio_sid = "twilio_sid"
        self.auth_token = "auth_token"
        self.twilio_num = "twilio_num"
        self.receiver_num = "receiver_num"
    
    # Send SMS to user to notify them of great flight deals.
    def notify(self, msg):
        client = Client(self.twilio_sid, self.auth_token)
        client.messages.create(body=msg, from_=self.twilio_num, to=self.receiver_num)
