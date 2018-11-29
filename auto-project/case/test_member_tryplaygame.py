import unittest
from common import base
from common.logger import Log


class MenberTryPlayGame(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test_Member_tryplaygame(self):
        '''试玩游戏'''
        route = "/unity/AB/playGame"
        url = "".join(base.get_url(route))
        json = {"siteCode": "ybh",
                "userName": "abTestUser002",
                "gameType": "live",
                "gameId": "af@1100"}
        kwargs = {"json": json}
        Method = "post"
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("---------start---------")
        self.assertIn("true" or "第三方不支持此功能", resp.text, msg="失败原因：%s not in %s" % ("true" or "第三方不支持此功能", resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")

if __name__ == "__main__":
    unittest.main()