import requests
#发请求
login_url = "http://localhost/index.php/?m=Home&c=User&a=do_login"
login_data = {
    "username" : "13800000000",
    "password" : "123456",
    "verify_code":"8888"
}
response = requests.post(url=login_url,data=login_data)

#响应
print(response.json())