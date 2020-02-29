import requests


class HTTPRequest:
    def __init__(self, website):
        self.website = str(website)
        self.session = requests.Session()
        self.content = None

    def make_request(self):
        self.content = self.session.get(self.website).content

    def __str__(self):
        return str(self.content)
