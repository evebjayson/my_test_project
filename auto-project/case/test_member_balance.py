import unittest
from common.logger import Log
from common import base


class MemberBalance(unittest.TestCase):

    def setUp(self):
        self.log = Log()
    def test_MemberBalance(self):
        '''查询余额'''
        route = "/unity/AB/queryqueryBalance"
        url = "".join(base.get_url(route))
        json = {"siteCode":"ybh",
	            "userName":"Wo6laX7wDtQj",
                }
        kwargs = {"json":json}
        Method = "post"
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("-------------start------------")
        self.assertEqual(resp.status_code,200,msg="失败原因：%s != %s" %(resp.status_code,200))
        self.log.info("----------test is pass----------")
        self.log.info("--------------end-------------")



if __name__ == "__main__":
    unittest.main()