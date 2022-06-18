from matplotlib.font_manager import json_dump

import requests
import json

headers ={
    "Authorization": "Bearer"
}

apikey="[APIKEY]" #UPDATE WITH YOUR ACCUWEATHER API KEY

def get_location_key():
    #curl -X GET "http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey=2Th2FmdD2N0HMOsGL7laIf02BtGW9q1G&q=30102"
    zipcode = '[ZIPCODE]' # UPDATE WITH YOUR ZIPCODE
    endpoint ="http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey={}&q={}".format(apikey,zipcode)
    #print("ENDPOINT: ",endpoint)
    #http://dataservice.accuweather.com/locations/v1/postalcodes/search?
    data = requests.get(endpoint)
    return data

def get_weather(locationkey):
    #curl -X GET "http://dataservice.accuweather.com/currentconditions/v1/12843_PC?apikey=2Th2FmdD2N0HMOsGL7laIf02BtGW9q1G"
    endpoint = "http://dataservice.accuweather.com/currentconditions/v1/{}?apikey={}&details=true".format(locationkey,apikey)
    data = requests.get(endpoint)
    return(data)

# LOGIC
location_key = get_location_key()
data = location_key.json()
#print(data)
location_keys = []
for each in data:
    #print(each['Code'])
    lockey = each['Key']
    #print(lockey)
    location_keys.append(lockey)
all_results ={}
try:
    results = get_weather(location_keys[0])
    full_results =results.json()
      
except:
    pass

for eachresult in full_results:
    print("Weather:{} -- Temp:{} F -- Humidity:{}% -- Rain:{}".format(eachresult['WeatherText'],eachresult['Temperature']['Imperial']['Value'],eachresult['RelativeHumidity'],eachresult['HasPrecipitation']))
