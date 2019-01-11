import unittest
from common import base,logger,login_token
from data.readexcel import ExcelUtil

data = ExcelUtil("MembershipManagement").dict_data()
class SaveAccount(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()
    def test_save_account(self):
        '''创建会员'''
        route = data[1]["route"]
        url = "".join(base.get_url(route))
        datas = {"loginName":base.generate_username_str(),
                 "loginPwd":base.generate_password_str(),
                 "groupId":1}
        token = login_token.login().get_token()
        header = eval(data[1]["header"])
        header["token"] = token
        kwargs = {"json": datas,"headers": header}
        Method = data[1]["method"]
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[1]["expect"], resp.text, msg="失败原因:%s not in %s" %(data[1]["expect"], resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")

if __name__=="__main__":
    unittest.main()