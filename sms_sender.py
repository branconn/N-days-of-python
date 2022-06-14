import os
from twilio.rest import Client
import dotenv
dotenv.load_dotenv()


class Sms:
    def __init__(self):
        self.ssid = os.getenv("TWILIO_SSID")
        self.token = os.getenv("TWILIO_TOK")
        self.sender = os.getenv("SENDING_PHONE")
        self.receiver = os.getenv("RECEIVING_PHONE")

    def send(self, text):
        client = Client(self.ssid, self.token)

        message = client.messages \
            .create(
                body=text,
                from_=self.sender,
                to=self.receiver
            )
        print(f"Message sent:\n{message}")
