import requests
url = "http://www.baidu.com"
#发送请求
response = requests.get(url)
#响应数据编码格式
print("原始数据的编码格式",response.encoding)
#设置编码
response.encoding = "utf-8"
#查看相应
print(response.text)