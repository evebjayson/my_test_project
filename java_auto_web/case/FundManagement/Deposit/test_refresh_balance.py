import unittest
from java_auto_web.common import logger,login_token,base
from java_auto_web.data.readexcel import ExcelUtil



data = ExcelUtil("PersonalCenter").dict_data()
class RefreshBalance(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_refresh_balance(self):
        '''刷新余额'''
        route = data[2]["route"]
        url = "".join(base.get_url(route) + "?" + login_token.login().get_token())
        header = eval(data[2]["header"])
        header["token"] = login_token.login().get_token()
        kwargs = {"headers":header}
        method = data[2]["method"]
        resp = base.get_response(url,method,**kwargs)
        self.log.info("----------test start----------")
        self.log.info("请求参数为: %s" %kwargs)
        self.log.info("响应内容为: %s" %resp.text)
        self.assertIn(data[2]["expect"],resp.text,msg="失败原因: %s not in %s" %(data[2]["expect"],resp.text))
        self.log.info("--------test is pass--------")
        self.log.info("----------end----------")


if __name__ == "__main__":
    unittest.main()