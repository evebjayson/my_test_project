import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil



data = ExcelUtil("PersonalCenter").dict_data()
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_login(self):
        '''获取取款页面'''
        route = data[4]["route"]
        url = "".join(base.get_url(route) + "?" + login_token.login().get_token())
        header = eval(data[4]["header"])
        header["token"] = login_token.login().get_token()
        kwargs = {"headers": header}
        method = data[4]["method"]
        resp = base.get_response(url, method, **kwargs)
        self.log.info("----------test start----------")
        self.log.info("请求参数为: %s" %kwargs)
        self.log.info("响应内容为: %s" %resp.text)
        self.assertIn(data[4]["expect"],resp.text,msg="失败原因: %s not in %s" %(data[4]["expect"],resp.text))
        self.log.info("--------test is pass--------")
        self.log.info("----------end----------")


if __name__ == "__main__":
    unittest.main()