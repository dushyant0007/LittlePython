import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)  # output ---> <Response [200]> // here 200 is response code
print(response.status_code)

# 1xx   --> Hold on somethind is happing this is not final
# 2xx  --> everything is successful
# 3xx  --> Go away // don't  have permession to excess
# 4xx  --> You screwed up
# 5xx  --> I screwed up

data = response.json()
print(data)
print(data["iss_position"])
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (latitude, latitude)

# ----------------------------------------------------------

my_lat = 51.507351
my_lng = -0.127758

parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted":0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# or
# response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={my_lat}&lng={my_lng}")
response.raise_for_status()
print(response.json())

#//
