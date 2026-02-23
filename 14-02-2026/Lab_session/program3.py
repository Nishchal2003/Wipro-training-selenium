#3.Write a test that checks an API health endpoint.If status code is not 200 → skip the test dynamically.

import requests
import pytest

def test_api_health():
    try:
        response = requests.get("https://api.restful-api.dev/objects")
        print(response)

    except requests.exceptions.RequestException as e:
        print(f"API not reachable {response.status_code}")

    if response.status_code != 200:
        pytest.skip(reason="status_code != 200")

    print("Successfull")