#to getpost
import requests
url =("https://sheguidesme.com/api/v1/posts/")
payload = {
    "content" :"Automation testing",
    "viewers_handle" :"Universal"
}
header = {
    "Content-Type" : "application/json",
    "Accept" : "application/json",
    "Authorization" :"token 9b9a50015a70fc28c4f46caf8985ac5b0e366af1"
}
response = requests.post(url, json= payload,headers=header)
status = response.status_code
print(response.json())
print(status)
