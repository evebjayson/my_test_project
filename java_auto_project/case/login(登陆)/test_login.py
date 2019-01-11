import unittest
from common import base,logger
from data.readexcel import ExcelUtil




data = ExcelUtil("login").dict_data()

class Login(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()

    def test_login(self):
        '''登陆'''
        route = data[0]["route"]
        url = "".join(base.get_url(route))
        kwargs = {"json":eval(data[0]["data"]),"headers":eval(data[0]["header"])}
        Method = data[0]["method"]
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("--------start--------")
        self.assertIn(data[0]["expect"],resp.text,msg="失败原因:%s not in %s"%(data[0]["expect"],resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")

if __name__=="__main__":
    unittest.main()

