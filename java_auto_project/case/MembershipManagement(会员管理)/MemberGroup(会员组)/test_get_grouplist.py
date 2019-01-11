import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipManagement").dict_data()
class grouplist(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_get_grouplist(self):
        '''获取会员组列表'''
        route = data[8]["route"]
        url = "".join(base.get_url(route))
        token = login_token.login().get_token()
        header = eval(data[8]["header"])
        header["token"] = token
        kwargs = {"json": token, "headers": header}
        Method = data[8]["method"]
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[8]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[8]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")



if __name__ == "__main__":
    unittest.main()