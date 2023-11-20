import requests
import json

#1
request = "https://api.chucknorris.io/jokes/random"


try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        joke_text = json_response['value']
        print("Chuck Norris joke:")
        print(joke_text)
    else:
        print("Failed to fetch Chuck Norris joke. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Request cannot be performed",e)


#2

def convert_F_to_C(k_degrees):
    c_degree = round(k_degrees - 273.15)
    return c_degree

API_key = "3d72969b3b3514e312556c73f2b2d554"
keyword = input("Give a name of a Municipality:\n ")

request = "http://api.openweathermap.org/data/2.5/weather?q=" + keyword + "&appid=" + API_key


try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        weather_description = json_response["weather"][0]["description"]
        print(f"The weather in {keyword} now is {weather_description}.")
        k_degrees = json_response["main"]["temp"]
        c_degree = convert_F_to_C(k_degrees)
        print(f"The temperature of {keyword} is {c_degree}")
except requests.exceptions.RequestException as e:
    print("Request cannot be performed")

