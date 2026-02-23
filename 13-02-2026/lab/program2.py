#Send a GET request with query parameter userId=2 and print number of posts returned.
import  requests

user_id = {
    "userId":2
}
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
    #or we can use response = requests.get( "https://jsonplaceholder.typicode.com/posts",params=user_id)
    if response.status_code == 200:
        posts = response.json()
        print("Number of posts recived",len(posts))
    else:
        print("Error")
except Exception as e:
    print("Error {e}")
