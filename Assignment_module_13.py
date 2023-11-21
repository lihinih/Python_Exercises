
#1
from flask import Flask, Response
import json

app = Flask(__name__)

def is_prime(number):
    number = int(number)
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/check_prime/<int:number>')
def check_prime(number):
    number = int(number)
    response = {
        "Number": int(number),
        "isPrime": is_prime(number)
    }

    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=200)
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1',port=5000)

#2

app = Flask(__name__)

airport_data = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGFF": {"Name": "Cardiff International Airport", "Location": "Cardiff"},
    "EGGD": {"Name": "Bristol Airport", "Location": "Bristol"}
}

@app.route('/airport/<icao_code>')
def get_airport_info(icao_code):
    icao_code = icao_code.upper()
    if icao_code in airport_data:
        airport_info = airport_data[icao_code]
        response_data = {
            "ICAO": icao_code,
            "Name": airport_info["Name"],
            "Location": airport_info["Location"]
        }
        json_response = json.dumps(response_data)
        http_response = Response(response=json_response, status=200, mimetype="application/json")
        return http_response
    else:
        error_response = {"error": "Airport not found"}
        json_error_response = json.dumps(error_response)
        http_error_response = Response(response=json_error_response, status=404, mimetype="application/json")
        return http_error_response


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=500)

