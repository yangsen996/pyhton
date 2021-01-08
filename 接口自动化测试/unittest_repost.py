#导报
import time
import unittest

#封装测试套件
suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite('测试类名'))
#指定报告路径
report = './report/report-{}.html'.format(time.strftime("%Y%m%d-%H%M%S"))
#打开文件
with open(report,"wb") as f:
    #创建运行器
    runner = HTMLTestRunner(f,title="接口测试报告")
#执行测试套件
    runner.run(suit)