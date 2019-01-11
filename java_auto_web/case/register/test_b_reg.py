import unittest
from java_auto_web.common import logger,base
from java_auto_web.data.readexcel import ExcelUtil


data = ExcelUtil("register").dict_data()
class Reg(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_reg(self):
        '''获取注册验证码'''
        route = data[1]["route"]
        url = "".join(base.get_url(route)) + base.create_random_numbers(6)
        header = eval(data[1]["header"])
        kwargs = {"headers": header}
        method = data[1]["method"]
        resp = base.get_response(url,method,**kwargs)
        self.log.info("----------test start----------")
        self.log.info("请求内容为: %s" %kwargs)
        self.log.info("请求接口为: %s" %url)
        self.log.info("响应内容为: %s" %resp.content)
        self.assertEqual(data[1]["expect"],resp.status_code,msg="失败原因: %s != %s" %(data[1]["expect"],resp.status_code))
        self.log.info("--------test ia pass--------")
        self.log.info("----------test end----------")


if __name__ == "__main__":
    unittest.main()



