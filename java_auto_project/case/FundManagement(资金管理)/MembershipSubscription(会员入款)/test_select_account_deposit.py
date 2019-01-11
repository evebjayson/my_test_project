import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipSubscription").dict_data()
class SelectaAccountDeposit(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_select_accountdepositlist(self):
        '''条件搜索会员存款'''
        route = data[1]["route"]
        url = "".join(base.get_url(route))
        url = "".join([url,data[1]["params"]])
        token = login_token.login().get_token()
        header = eval(data[1]["header"])
        header["token"] = token
        kwargs = {"json": token, "headers": header}
        Method = data[1]["method"]
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("--------start--------")
        self.log.info("获取的token:%s" %token)
        self.assertIn(data[1]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[1]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")

if __name__ == "__main__":
    unittest.main()