#Write a POST request to create a new resource and verify status code 201.
import  requests

try:
    data = {
        "userId": 1,
        "tittle": "APIs",
        "body": "I am created"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
    if response.status_code == 200:
        print("Resources created\nstatus_created,\nResponse json","",response.status_code,response.json() )
    else:
        print("Error status_code:",response.status_code)
except Exception as e:
    print("Error {e}")
