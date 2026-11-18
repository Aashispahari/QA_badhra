#using put method
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "userId": 1,
        "title": "Api title",
        "body": "Api" 
    }

headers = {
    "Authorization": "token asjdfbhalsidbf"
}
response = requests.put(url, json=payload, headers=headers)
status = response.status_code
print(response.json())
print(status)