import requests


class AuthApi:
    def __init__(self, url):
        self.url = url

    def login(self, username, password):
        response = requests.post(
            self.url + "/auth/login",
            json={
                "username": "harrypotter",
                "password": "expelliarmus"
            }
        )

        return response
