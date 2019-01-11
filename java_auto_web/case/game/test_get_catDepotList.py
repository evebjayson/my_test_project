import unittest
from java_auto_web.common import logger,login_token,base
from java_auto_web.data.readexcel import ExcelUtil

data = ExcelUtil("game").dict_data()
class GetGameList(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()

    def test_get_catDepotList(self):
        route = data[0]["route"]
        parameters = data[0]["parameters"]
        for parameter in parameters:
            url = "".join(base.get_url(route) + "?" + "catId=" + str(parameter))
        header = eval(data[0]["header"])
        kwargs = {"headers": header}
        method = data[0]["method"]
        resp = base.get_response(url,method,**kwargs)
        self.log.info("---------test start----------")
        self.log.info("请求内容为: %s" %kwargs)
        self.log.info("响应内容为: %s " %resp.json())
        self.assertEqual(data[0]["expect"],resp.json()["msg"],msg="失败原因: %s != %s" %(data[0]["expect"],resp.json()["msg"]))
        self.log.info("----------test is pass----------")
        self.log.info("----------test end----------")


if __name__ == "__main__":
    unittest.main()