import requests

url = "https://jsonplaceholder.typicode.com/users"

customer_data = {
    "name": "Nishchal",
    "email": "nmu@gmail.com",
    "balance": 5000
}

customer_id = None


def test_create_customer():
    global customer_id

    response = requests.post(url, json=customer_data)
    assert response.status_code == 201

    data = response.json()
    customer_id = data["id"]

    assert data["name"] == customer_data["name"]


def test_get_customer():
    response = requests.get(f"{url}/{customer_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == customer_id


def test_update_customer():
    update_data = {
        "id": customer_id,
        "name": "Nishchal",
        "email": "umapathi@gmail.com",
        "balance": 5000
    }

    response = requests.put(f"{url}/{customer_id}", json=update_data)
    assert response.status_code == 200

    data = response.json()
    assert data["email"] == update_data["email"]