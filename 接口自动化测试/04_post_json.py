import requests

login_url = ""
login_data = {

}
response = requests.post(url = login_url,json=login_data)

print(response.json())