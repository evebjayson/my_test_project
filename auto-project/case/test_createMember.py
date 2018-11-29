import unittest
from common.logger import Log
from common import base
from data.readexcel import ExcelUtil

data = ExcelUtil().dict_data()
class createMember(unittest.TestCase):

    def setUp(self):
        self.log = Log()
    def test_createMember(self):
        '''创建会员'''
        route =data[0]["route"]
        url = "".join(base.get_url(route))
        json = {"siteCode":"ybh",
                "userName":base.generate_username_str()}
        kwargs = {"json": json}
        Method = "post"
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("---------start---------")
        self.assertIn("true",resp.text,msg="失败原因：%s not in %s"%("true",resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")

if __name__ == "__main__":
    unittest.main()
print("------")