'''
验证码 http://localhost/index.php?m=Home&c=User&a=verify
 登录 http://localhost/index.php?m=Home&c=User&a=do_login
'''

import requests
import unittest
#创建测试类
class TpshopLogin(unittest.TestCase):

    #创建测试方法
    #setup
    def setUp(self) -> None:
        #实例化session
        self.session = requests.Session()
        #定义验证码接口
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
        #定义登录接口
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
    #teardown
    def tearDown(self) -> None:
        self.session.close()
    #登录成功
    def test01_succes(self):
        #返送验证码请求断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200,response.status_code)
        self.assertIn("image",response.headers.get("Content-Type"))
        #发送登录请求并断言
        login_data = {
            "username" : "13800000000",
            "password" : "123456",
            "verify_code" : "8888"
        }
        response = self.session.post(url=self.url_login,data=login_data)
        print(response.json())
        self.assertEqual(200,response.status_code)
        self.assertEqual(1,response.json().get("status"))
        self.assertIn("登陆成功",response.json().get("msg"))
    #账号不存在
    def test02_user_is_not_exist(self):
        # 返送验证码请求断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录请求并断言
        login_data = {
            "username": "1380000011",
            "password": "123456",
            "verify_code": "8888"
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))
    #验证码错误
    def test03_verify_err(self):
        # 返送验证码请求断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录请求并断言
        login_data = {
            "username": "13800000000",
            "password": "error",
            "verify_code": "8888"
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))