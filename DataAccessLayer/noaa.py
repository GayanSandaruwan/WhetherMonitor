from DataAccessLayer.XMLHandler import XMLHandler
import requests

class NOAA:
    token=None;
    xmlHandler = None;

    def __init__(self):
        NOAA.xmlHandler = XMLHandler();
        tokenKey = NOAA.xmlHandler.getToken("noaa");
        NOAA.token = {'token' : tokenKey};
        pass

    @staticmethod
    def getData(dataType):
        url = NOAA.xmlHandler.getURL(dataType,"noaa");
        response = requests.get(url, headers=NOAA.token);
        data = response.json();
        return data;
