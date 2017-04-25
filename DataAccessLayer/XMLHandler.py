import lxml.etree as etree
from bs4 import BeautifulSoup;


class XMLHandler:

    doc= None;
    soup =  None;
    def __init__(self):
        XMLHandler.soup = BeautifulSoup(open("..//Config.xml"),"lxml")
        pass

    @staticmethod
    def getURL(dataType,portal):                   # Function Returns the URL for a requested Data type
        urls = XMLHandler.soup.find("url",datatype=dataType,portal=portal)
        return urls.text

    @staticmethod
    def getToken(portal):
        token = XMLHandler.soup.find("token",portal=portal);
        return token.text;
