import requests
url= ("https://sheguidesme.com/api/v1/myposts/10286/")
header = {
    "Authorization":"token 9b9a50015a70fc28c4f46caf8985ac5b0e366af1"
}
response = requests.delete(url, headers=header)
print(response.status_code)

