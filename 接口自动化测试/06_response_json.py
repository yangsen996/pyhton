import requests
url = ""
response = requests.get(url)
print(response.json())