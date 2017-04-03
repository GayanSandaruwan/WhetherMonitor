import requests
from .XMLHandler import XMLHandler

token = {'token':'ycfAHUIUtBJyyTalPLJMOStImABViIrU'}
#url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCNDMS&locationid=ZIP:28801&startdate=2010-09-01&enddate=2010-09-01"
url = XMLHandler.getURL("trail");
print(url);
#response = requests.get(url, headers = token) 
#data = response.json()

#print (data)




