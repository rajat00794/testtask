import requests


class Smsservice:
    def __init__(self, smsconfig: object) -> None:
        self.config = smsconfig

    def send_msg(self, phone, msg):
        print(self.config.get_sms_uri(phone, msg))
        data = requests.get(self.config.get_sms_uri(phone, msg))
        return data.content
