import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipSubscription").dict_data()
class Detailsofpayment(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_details_of_payment(self):
        '''获取会员出款详情'''
        route = data[4]["route"]
        url = "".join(base.get_url(route))
        token = login_token.login().get_token()
        header = eval(data[4]["header"])
        header["token"] = token
        kwargs = {"json": token, "headers": header}
        Method = data[4]["method"]
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[4]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[4]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")

if __name__ == "__main__":
    unittest.main()