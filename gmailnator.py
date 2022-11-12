import requests
import time

class Gmailnator:
    def __init__(self):
        self.session = requests.Session()
        self.session.get("https://www.emailnator.com/")
        self.headers = {
            "x-xsrf-token": requests.utils.unquote(self.session.cookies["XSRF-TOKEN"]),
        }
        self.__email = ""

    def generate_email(self):
        json = {
            "email": [
                "plusGmail",
                "dotGmail"
            ]
        }
        self.__email = self.session.post("https://www.emailnator.com/generate-email", json=json, headers=self.headers).json()["email"][0]

    def get_email(self):
        return self.__email

    def get_inbox(self, wait=False):
        json = {
            "email": self.__email
        }
        inbox = lambda : self.session.post("https://www.emailnator.com/message-list", json=json, headers=self.headers).json()["messageData"]
        if wait:
            while len(inbox()) == 1:
                time.sleep(1)
        return inbox()[1:]
