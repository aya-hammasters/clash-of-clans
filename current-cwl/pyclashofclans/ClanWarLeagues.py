import urllib
import json

class ClanWarLeagues:
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
    Get the current war league group for a specific clan tag
    """
    def get_current_leaguegroup(self, tag):
        return self.get('/clans/%23' + tag.strip('#') + "/currentwar/leaguegroup")

    """
    Get rounds for a particular war tag. 
    War tags are part of the data returned by get_current_leaguegroup()
    """
    def get_wartag(self, wartag):
        return self.get('/clanwarleagues/wars/%23' + wartag.strip('#'))
