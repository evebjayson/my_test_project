import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil

data = ExcelUtil("MembershipManagement").dict_data()
class AuditReduce(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_Reduce_balances(self):
        '''减少余额'''
        route = data[6]["route"]
        url = "".join(base.get_url(route))
        header = eval(data[6]["header"])
        header["token"] = login_token.login().get_token()
        json = eval(data[6]["data"])
        kwargs = {"json":json,"headers": header}
        Method = data[6]["method"]
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[6]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[6]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")



if __name__ == "__main__":
    unittest.main()