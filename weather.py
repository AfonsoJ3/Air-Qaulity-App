from tkinter import *
from PIL import Image
from PIL import ImageTk as ITK
import requests as rq
import json

root = Tk()
root.title("Weather App")
#root.iconbitmap('')
root.geometry('400x400')

try:
    api_request = rq.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=02302&distance=5&API_KEY=51EF9F29-ED44-4A44-AF62-86B538033B1E") 
    api = json.loads(api_request.content)

    city = api[0]["ReportingArea"]
    state = api[0]["StateCode"]
    latitude = api[0]["Latitude"]
    longitude = api[0]["Longitude"]
    aqi = api[0]["AQI"]
    category = api[0]["Category"]["Name"]


except Exception as e:
    api = "Error..."

myLabel = Label(root, text= f"City: {city} state:{state} latitute:{latitude} longitute:{longitude} air quality:{aqi} category: {category}")
myLabel.pack()

root.mainloop()
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=02302&distance=25&API_KEY=51EF9F29-ED44-4A44-AF62-86B538033B1E