import requests
url = ("https://sheguidesme.com/api/v1/myposts/10281/")
payload = {
    "content":"Edit from python",
    "viewers_handle" :"Universal"
}
header = {
    "Content-Type" : "application/json",
    "Accept": "application/json",
    "Authorization" : "token 9b9a50015a70fc28c4f46caf8985ac5b0e366af1"
}
response = requests.patch(url,headers=header,json = payload)
print(response.status_code)


# print(response.json())
