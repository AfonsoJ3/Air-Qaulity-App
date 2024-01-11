from tkinter import *
from PIL import Image
from PIL import ImageTk as ITK
import requests as rq
import json
 


def color(category):
    quality = category
    
    if not quality:
        return None

    if quality.lower() == "good":
        return 'green' 
    elif quality.lower() == "moderate":
        return 'yellow'
    elif quality.lower() == "unhealthy for sensitive groups":
        return 'orange'
    elif quality.lower() == "unhealthy":
        return 'red'
    elif quality.lower() == "very unhealthy":
        return 'purple'
    elif quality.lower() == "hazardous":
        return 'black'

    return None
root = Tk()
root.title("Weather App")
#root.iconbitmap('')
root.geometry('500x100')


try:
    api_request = rq.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=02302&distance=5&API_KEY=51EF9F29-ED44-4A44-AF62-86B538033B1E") 
    api = json.loads(api_request.content)

    city = api[0]["ReportingArea"]
    state = api[0]["StateCode"]
    latitude = api[0]["Latitude"]
    longitude = api[0]["Longitude"]
    aqi = api[0]["AQI"]
    category = api[0]["Category"]["Name"]

    
    colors = color(category)
    root.configure(background=colors)


    if not colors:
        raise ValueError ()

    if colors == 'black':
        myLabel = Label(root, text= f"City: {city}, State:{state} \nLatitute:{latitude}, Longitute:{longitude} \nAir Quality:{aqi}, Category: {category}",
                font=("TimeNewRoman", 20), background=colors, foreground='white')    

    else:
        myLabel = Label(root, text= f"City: {city}, State:{state} \nLatitute:{latitude}, Longitute:{longitude} \nAir Quality:{aqi}, Category: {category}",
                font=("TimeNewRoman", 20), background=colors)
    
    

except Exception as e:
    api = "Error..."
    myLabel = Label(root, text= api, font=("TimeNewRoman", 20))


myLabel.pack()
root.mainloop()


