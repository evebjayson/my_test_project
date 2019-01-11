import unittest
from common import logger,login_token,base
from data.readexcel import ExcelUtil


data = ExcelUtil("MembershipManagement").dict_data()
class SelectGroup(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()

    def test_select_grouplist(self):
        '''查询会员组'''
        route = data[9]["route"]
        url = "".join(base.get_url(route))
        url = "".join([url, data[9]["params"]])
        token = login_token.login().get_token()
        header = eval(data[9]["header"])
        header["token"] = token
        kwargs = {"json": token, "headers": header}
        Method = data[9]["method"]
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[9]["expect"], resp.text, msg="失败原因:%s not in %s" % (data[9]["expect"], resp.text))
        self.log.info("------test is pass------")
        self.log.info("---------end---------")



if __name__=="__main__":
    unittest.main()