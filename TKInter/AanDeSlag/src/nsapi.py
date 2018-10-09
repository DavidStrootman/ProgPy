import requests
import xmltodict


class NSApi:
    """NSApi"""

    api_url = "http://webservices.ns.nl"
    api_url_avt = api_url + "/ns-api-avt"
    api_url_stationslist = api_url + "/ns-api-stations-v2"
    api_url_reisplanner = api_url + "/ns-api-treinplanner"

    def __init__(self, username, password):
        # Save auth info
        self.auth_details = (username, password)

    def get_stations(self):
        """Return list of station names"""

        # GET data and parse into xmldict
        response = requests.get(self.api_url_stationslist, auth=self.auth_details)
        xmldict = xmltodict.parse(response.text)

        # Create list
        stations = []

        # Load all Namen.Lang into list
        for station in xmldict["Stations"]["Station"]:
            stations.append(station["Namen"]["Lang"])

        return stations

    def actuele_vertrektijden(self, station):
        # Create request data dict
        data = {"station": station}

        # Request and return data in dict
        response = requests.get(self.api_url_avt, auth=self.auth_details, params=data)
        return xmltodict.parse(response.text)
