#Write a Python script to send a GET request to
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        users = response.json()

        for user in users:
            for key, value in user.items():
                print(f"{key}: {value}")
    else:
        print("Error: Occured")
except Exception as e:
    print("Error occured {e}")
