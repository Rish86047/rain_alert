import requests
from twilio.rest import Client

API_KEY = "your api key"
account_sid = "twilio account sid"
auth_token = "twilio auth token"

parameter = {"lat": 26.449923, "lon": 80.331871, "appid": API_KEY, "cnt": 4}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameter)
weather_data = response.json()
for i in weather_data["list"]:
    condition_code = i["weather"][0]["id"]
    if condition_code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It will rain today , it's cloudy outside.",
            from_="your twilio number",
            to="your twilio registered number"
        )
        print(message.status)
