import requests
from twilio.rest import Client

# Environment variables
#  These variables have values in string
# Creating env variable -->   export  _nameOfVariable_=_value_
# import os
#  key = os.environ.get("_nameOfVariable")

owm_endPoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5e5f560be1e6f47d076f5cd8619d0e0f"

account_sid = "ACe0d8014be4ad4cc4e79466e6802039b8"
auth_token = "d78d091cc48384d5de3545e86ecd3085"

weather_params = {
    "lat": 26.827021,
    "lon": 75.857454,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(owm_endPoint, params=weather_params)
response.raise_for_status()
print(response)
weather_data = response.json()
weather_slice = weather_data["hourly"][0:12]
# print(weather_slice)
# print(weather_data)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bringa an Umbrella ☂️☔️☂️☔️☂️☔️ ",
        from_='+18288822942',
        to='+919309068020'
    )

    print(message.status)
    print(message.sid)

sms = weather_slice[0]["weather"][0]["description"]


client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=f" {sms} ",
    from_='+18288822942',
    to='+919309068020'
)

print(message.status)
print(message.sid)
