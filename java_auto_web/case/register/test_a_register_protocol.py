import unittest
from java_auto_web.common import logger,base
from java_auto_web.data.readexcel import ExcelUtil


data = ExcelUtil("register").dict_data()
class RegisterProtocol(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_register_protocol(self):
        '''注册协议'''
        route = data[0]["route"]
        url = "".join(base.get_url(route))
        header = eval(data[0]["header"])
        kwargs = {"headers":header}
        method = data[0]["method"]

        resp = base.get_response(url,method,**kwargs)
        self.log.info("----------test start----------")
        self.log.info("请求内容为: %s" %kwargs)
        self.log.info("响应内容为: %s" %resp.text)
        self.assertIn(data[0]["expect"],resp.text,msg="失败原因: %s not in %s" %(data[0]["expect"],resp.text))
        self.log.info("--------test is pass--------")
        self.log.info("----------test end----------")

if __name__ == "__main__":
    unittest.main()