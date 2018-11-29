import unittest
from common import base
from common.logger import Log

'''有些平台是需要先打开游戏大厅，有点不需要，不需要的平台会返回：第三方不支持'''
class MenberOpenHall(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test_Menber_openHall(self):
        '''打开游戏大厅'''

        route = "/unity/AB/openHall"
        url = "".join(base.get_url(route))
        json = {"siteCode": "ybh",
                "userName": "abTestUser002"}
        kwargs = {"json": json}
        Method = "post"
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("---------start---------")
        self.assertIn("true" or "第三方不支持此功能", resp.text, msg="失败原因：%s not in %s" % ("true" or "第三方不支持此功能", resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")


if __name__ == "__main__":
    unittest.main()