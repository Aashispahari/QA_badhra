#to delete

import requests
url = ("https://jsonplaceholder.typicode.com/posts/1")
response = requests.delete(url)
status = response.status_code
print(status)
# if status == 200:
#     print(f"post delete sucesfully {status}")
# else:
#     print(f"{status} Failed to delete post ")import requests
url= ("https://sheguidesme.com/api/v1/myposts/10286/")
header = {
    "Authorization":"token 9b9a50015a70fc28c4f46caf8985ac5b0e366af1"
}
response = requests.delete(url, headers=header)
print(response.status_code)

