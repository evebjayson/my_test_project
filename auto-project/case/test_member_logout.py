import unittest
from common.logger import Log
from common import base

class MemberLogin(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test_member_login(self):
        '''会员登陆'''
        route = "/unity/AB/logout"
        url = "".join(base.get_url(route))
        json = {"siteCode": "ybh",
                "userName": "abTestUser002"
                }
        kwargs = {"json": json}
        Method = "get"
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("---------start---------")
        self.assertIn("true" or "第三方不支持此功能", resp.text, msg="失败原因：%s not in %s" % ("true" or "第三方不支持此功能", resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")


if __name__ == "__main__":
    unittest.main()