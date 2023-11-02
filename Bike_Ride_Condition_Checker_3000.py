import tkinter as tk
import requests

# Bike text art
bike_art = r"""
   __o
_ \<_
(_)>(_)
"""

# Function to fetch weather data and determine the result
def check_bike_ride():
    api_key = "fb78a0cbdcf0d89cd463cd6e9650b621"
    lat = 52.3548
    lon = 4.9497

    # Making the API request
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        wind_speed = data["wind"]["speed"]
        wind_direction = data["wind"]["deg"]
        rain_volume = data.get("rain", {}).get("1h", 0)

        # Setting the scenarios
        if wind_speed > 15:
            result_label.config(text="Just take the train: Extremely high wind speed.", font=("Helvetica", 14, "bold"))
        elif wind_speed > 9 and wind_direction >= 45 and wind_direction <= 135:
            result_label.config(text="You should take the train: Moderate to high wind speed with north wind direction.", font=("Helvetica", 14, "bold"))
        elif (wind_speed > 6 and rain_volume > 44) or (wind_speed > 10 and rain_volume > 34):
            result_label.config(text="Don't bother, take the train: Moderate to high wind speed with high rain volume.", font=("Helvetica", 14, "bold"))
        elif wind_speed > 7 and wind_direction >= 135 and wind_direction <= 225:
            result_label.config(text="TURBO BOOST! The wind is extremely favorable for the bike route.", font=("Helvetica", 14, "bold"))
        else:
            result_label.config(text="You're taking the bike buddy!", font=("Helvetica", 14, "bold"))
    else:
        result_label.config(text="API request failed. Status code: " + str(response.status_code), font=("Helvetica", 14, "bold"))

# Creating a Tkinter window
root = tk.Tk()
root.title("Bike Ride Condition Checker 3000.exe")

# Setting the window size (width x height)
window_width = 400  # Set the desired width
window_height = 280  # Set the desired height
root.geometry(f"{window_width}x{window_height}")

# Creating a label for the bike art
bike_art_label = tk.Label(root, text=bike_art, font=("Courier", 20))
bike_art_label.pack()

# Creating a button to check bike ride conditions
check_button = tk.Button(root, text="Press to check bike ride conditions", command=check_bike_ride, font=("Helvetica", 14, "italic"))
check_button.pack()

# Creating a label for the result (initially empty)
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
