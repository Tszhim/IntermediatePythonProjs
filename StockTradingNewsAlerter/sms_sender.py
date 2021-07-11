from twilio.rest import Client

class SMSSender:

    # Setting default values and preparing to send text message.
    def __init__(self, SMS):
        self.twilio_sid = "your twilio sid"
        self.auth_token = "your twilio auth token"
        self.sender = "your twilio phone number"
        self.receiver = "your phone number"
        self.sms = SMS
        self.send_sms()
    
    # Sending text message.
    def send_sms(self):
        
        # Setting up Twilio client and indicating addresses.
        client = Client(self.twilio_sid, self.auth_token)
        message = client.messages.create(
            body=self.sms,
            from_=self.sender,
            to=self.receiver
        )
        print(message.status)
