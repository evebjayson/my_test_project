import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipManagement").dict_data()
class OnlineAccount(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_get_onlineaccount(self):
        '''查询会员组'''
        route = data[10]["route"]
        url = "".join(base.get_url(route))
        url = "".join([url, data[10]["params"]])
        token = login_token.login().get_token()
        header = eval(data[10]["header"])
        header["token"] = token
        kwargs = {"json": token, "headers": header}
        Method = data[10]["method"]
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[10]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[10]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")



if __name__=="__main__":
    unittest.main()