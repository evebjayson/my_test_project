import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipManagement").dict_data()
class accountlist(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_get_accountlist(self):
        '''获取会员列表'''
        route = data[0]["route"]
        url = "".join(base.get_url(route))
        header = eval(data[0]["header"])
        header["token"] = login_token.login().get_token()
        kwargs = {"headers": header}
        Method = data[0]["method"]
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("--------获取会员列表 start--------")
        self.assertIn(data[0]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[0]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")


if __name__ == "__main__":
    unittest.main()