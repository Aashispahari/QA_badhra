import requests
url = ("https://sheguidesme.com/profile/me")
response = requests.get(url)
status = response.status_code
print(status)
# print(response.json())