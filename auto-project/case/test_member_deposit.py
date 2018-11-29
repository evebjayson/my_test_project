import unittest
from common.logger import Log
from common import base

class MemberDeposit(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test_Member_deposit(self):
        '''会员存款'''
        route = "/unity/FUN/deposit"
        url = "".join(base.get_url(route))
        json = {"siteCode": "AB",
                "userName": "test011",
                "orderNo":base.generate_orderNo_deposit_str(12),
                "amount": 1}
        kwargs = {"json": json}
        Method = "post"
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("---------start---------")
        self.assertIn("true",resp.text,msg="失败原因：%s not in %s" %("true",resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")


if __name__ == "__main__":
    unittest.main()
