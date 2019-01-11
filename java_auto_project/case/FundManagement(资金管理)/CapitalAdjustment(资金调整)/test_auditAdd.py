import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipManagement").dict_data()
class AuditAdd(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_add_balances(self):
        '''增加余额'''
        route = data[5]["route"]
        url = "".join(base.get_url(route))
        header = eval(data[5]["header"])
        header["token"] = login_token.login().get_token()
        json = eval(data[5]["data"])
        kwargs = {"json":json,"headers": header}
        Method = data[5]["method"]
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[5]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[5]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")





if __name__ == "__main__":
    unittest.main()