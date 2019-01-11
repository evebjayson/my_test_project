import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipSubscription").dict_data()
class IntraAccountTransfer(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()
    def test_get_intra_account_transfer(self):
        '''获取户内转账列表'''
        route = data[5]["route"]
        url = "".join(base.get_url(route))
        url = "".join([url,data[5]["params"]])
        token = login_token.login().get_token()
        header = eval(data[5]["header"])
        header["token"] = token
        kwargs = {"json": token, "headers": header}
        Method = data[5]["method"]
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[5]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[5]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")

if __name__ == "__main__":
    unittest.main()