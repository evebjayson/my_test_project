import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipManagement").dict_data()
class SelectaAccountList(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_select_accountlist(self):
        '''查询会员列表'''
        route = data[2]["route"]
        url = "".join(base.get_url(route))
        url = "".join([url,data[2]["params"]])
        token = login_token.login().get_token()
        header = eval(data[2]["header"])
        header["token"] = token
        kwargs = {"json": token, "headers": header}
        Method = data[2]["method"]
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("--------start--------")
        self.log.info("获取的token:%s" %token)
        self.assertIn("success", resp.text, msg="失败原因:%s not in %s" % ("success", resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")

if __name__ == "__main__":
    unittest.main()