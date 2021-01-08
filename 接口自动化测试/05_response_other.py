'''http://www.baidu.com'''
import requests

response = requests.get("http://www.baidu.com")

#响应状态码
print("响应状态码",response.status_code)
#请求url
print(response.url)
#字符编码
print(response.encoding)
#响应头数据
print(response.headers)
print("Content-Type:",response.headers.get("Content-Type"))
#响应cookie数据
print(response.cookies)
print(response.cookies.get("BDORZ"))
#文本形式响应
print(response.text)
#字节形式
print(response.content)
print(response.content.decode("utf-8"))