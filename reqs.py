import requests 
url="https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
# print(f"The status code is: {response.status_code}")
# print(response.json())
status = response.status_code

# if status == 200:
#     print("The requests was successfull")
# else:
#     print(f"The request was unsuccessfull with {status} code")


#assertion in python
assert status == 200,"The status code was not 300 "
print("Request was succesfull")


