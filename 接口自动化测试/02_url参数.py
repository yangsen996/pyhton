#导报
import requests
#发送请求
#url = "http://localhost/index.php/Home/Goods/search.html?q=iphone"
#response = requests.get(url)

#传递参数params
urlA = "http://localhost/index.php/Home/Goods/search.html"
#stringA = "q=iphone"
#response = requests.get(urlA,params=stringA)
#字典
dictA = {
    "q":"iphone"
}
response = requests.get(urlA,params=dictA)
#查看响应
print(response.text)