import urllib
import json

class Players:
    """
    A simple client library for the Clash of Clans API in python
    """
    def __init__(self, token):
        import requests
        self.requests = requests
        self.token = token
        self.api_endpoint = "https://api.clashofclans.com/v1"
        self.timeout = 30

    """
    Generic get method to the API
    """
    def get(self, uri, params=None):
        headers = {
            'Accept': "application/json",
            'authorization': "Bearer " + self.token
        }

        url = self.api_endpoint + uri
        
        if params:
            params = json.dumps(params)

        try:
            response = self.requests.get(url, data=params, headers=headers, timeout=30)
            return response.json()
        except:
            if 400 <= response.status_code <= 599:
                return "Error " + response.status_code

    """
    Find a specific player by player tag (omit # symbol)
    ex: #123456 would be
    client.find("123456")
    """
    def find(self, tag):
        return self.get('/players/%23' + tag.strip('#'))
