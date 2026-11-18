#create post using requests

import requests 
url="https://jsonplaceholder.typicode.com/posts"
payload =  {
    "userId": 1,
    "title": "Api title",
    "body": "Api body"
     }

response = requests.post(url,json=payload)
# print(response.status_code)
# print(response.json())
status = response.status_code
# assert status== 201,"Not created"
# print("post created sucessfully")

if status == 201:
    print(f"Post created with {status} code")
else:
    print(f"Unable to creat post {status}")

