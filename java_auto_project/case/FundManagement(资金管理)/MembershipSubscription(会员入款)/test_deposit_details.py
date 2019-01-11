import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipSubscription").dict_data()
class Depositetails(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_get_depositlist(self):
        '''获取会员存款详情'''
        route = data[2]["route"]
        url = "".join(base.get_url(route))
        token = login_token.login().get_token()
        header = eval(data[2]["header"])
        header["token"] = token
        kwargs = {"json": token, "headers": header}
        Method = data[2]["method"]
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[2]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[2]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")

if __name__ == "__main__":
    unittest.main()