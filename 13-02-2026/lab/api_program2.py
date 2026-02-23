import requests

from api import response

try:
    response = requests.get("http://127.0.0.1:5000/users")
    if response.status_code == 200:
        print("Ststus code is 200")

        data = response.json()
        print(data)
    else:
        print("error")

except Exception as e:
    print("Error occured {e}")