import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil



data = ExcelUtil("PersonalCenter").dict_data()
class TieOnCard(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def debug_test_tie_on_card(self):
        '''绑定银行卡'''
        route = data[5]["route"]
        url = "".join(base.get_url(route) + "?" + login_token.login().get_token())
        header = eval(data[5]["header"])
        header["token"] = login_token.login().get_token()
        json = {"address":base.create_random_address(),
                "cardNo":base.create_bank_cardNo(16),
                "bankName":base.read_random_bankname(),
                "city":base.read_random_provincename()}
        kwargs = {"json":json,"headers": header}
        method = data[5]["method"]
        resp = base.get_response(url, method, **kwargs)
        self.log.info("----------test start----------")
        self.log.info("请求参数为: %s" %kwargs)
        self.log.info("响应内容为: %s" %resp.text)
        self.assertIn(data[5]["expect"],resp.text,msg="失败原因: %s not in %s" %(data[5]["expect"],resp.text))
        self.log.info("--------test is pass--------")
        self.log.info("----------end----------")


if __name__ == "__main__":
    unittest.main()