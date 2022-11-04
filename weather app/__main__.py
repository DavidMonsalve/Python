import requests

API_KEY = "" #in order for this app to work you'd have to type in an Api key.
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    print(weather)
    temperature = data["main"]["temp"] - 273.15
    print(str(round(temperature)) + " C")
else:
    print("An error occurred. ")

input("Press enter to end. ")