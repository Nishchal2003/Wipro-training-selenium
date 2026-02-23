import requests
try:
    response = requests.get("https://api.restful-api.dev/objects")
    print(response)

    if response.status_code == 200:
        print("Status code is 200 k")
        #parse data
        data = response.json()
        print(data)

    else:
        print("Error : Occured")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")