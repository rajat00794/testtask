import os


class Config:
    API_KEY = os.getenv("api_key")
    SMS_URL = os.getenv("sms_url")

    def get_sms_uri(self, phone, msg):
        return f"{self.SMS_URL}:{self.API_KEY}/SMS/:{phone}/:{msg}/"
