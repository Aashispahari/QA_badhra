#to delete

import requests
url = ("https://jsonplaceholder.typicode.com/posts/1")
response = requests.delete(url)
status = response.status_code
print(status)
# if status == 200:
#     print(f"post delete sucesfully {status}")
# else:
#     print(f"{status} Failed to delete post ")