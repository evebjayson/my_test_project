import unittest
from common import base
from common.logger import Log

class MemberPlayGame(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test_Member_playGame(self):
        '''玩游戏'''
        route = "/unity/AB/playGame"
        url = "".join(base.get_url(route))
        json = {"siteCode": "ybh",
                "userName": "abTestUser002",
                "gameType":"live",
                "gameId":"af@1100"}
        kwargs = {"json": json}
        Method = "post"
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("---------start---------")
        self.assertIn("true",resp.text,msg="失败原因: %s not in %s"%("true",resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")


if __name__ == "__main__":
    unittest.main()

