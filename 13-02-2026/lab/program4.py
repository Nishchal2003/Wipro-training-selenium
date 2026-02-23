#Write code to check if response status code is not 200 and raise an exception.
import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}")

    print("Success ")
    print(response.json())

except Exception as e:
    print(f"Error: {e}")
