import tkinter as tk
import requests
import time

def getWeather():
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cb86b874a4f469150dcfa64dd80e8e9f"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info, font=("Helvetica", 20))
    label2.config(text = final_data, font=("Helvetica", 12))

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather Forecast App")

def on_entry_click(event):
    if textfield.get() == 'Enter the city':
       textfield.delete(0, "end") # delete all the text in the entry
       textfield.insert(0, '') #Insert blank for user input
       textfield.config(fg = 'black')

def on_focusout(event):
    if textfield.get() == '':
        textfield.insert(0, 'Enter the city')
        textfield.config(fg = 'grey')

textfield = tk.Entry(canvas, font=("Helvetica", 18), fg='grey')
textfield.insert(0, 'Enter the city')
textfield.bind('<FocusIn>', on_entry_click)
textfield.bind('<FocusOut>', on_focusout)
textfield.pack(pady=20)

submit_button = tk.Button(canvas, text="Get Weather", command=getWeather, font=("Helvetica", 14))
submit_button.pack()

label1 = tk.Label(canvas, font=("Helvetica", 30))
label1.pack()

label2 = tk.Label(canvas, font=("Helvetica", 12))
label2.pack()

canvas.mainloop()
