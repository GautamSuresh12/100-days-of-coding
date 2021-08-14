import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "76fe31353bb104eef85394c47ecd0cbc"
account_sid = "ACa1b8169531eb86d2bb30d6179de8534a"
auth_token = "c5761ab90e07f54f782938d702de9855"

weather_params = {
    "lat" : 9.925201,
    "lon" : 78.119774,
    "appid": api_key,
    "exclude" : "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+13478481871',
        to='+919150135016'
    )

    print(message.status)
