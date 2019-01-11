import unittest
from java_ui_auto_project.common import base,logger,cof
import time
from java_ui_auto_project.data.readexcel import ExcelUtil


data = ExcelUtil().dict_data()
class GetLoginPage(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
        self.driver = cof.get_driver()
    def test_get_loginpage(self):
        url = base.get_url(data[0]["route"])
        self.driver.get(url)
        time.sleep(3)
        text = self.driver.find_element_by_xpath(eval(data[0]["Xpath"])["查找元素"]).text
        self.log.info("--------start--------")
        self.assertEqual(data[0]["expect"],text,msg="失败原因:期望值:%s not same 实际值:%s" % (data[0]["expect"], text))
        self.log.info("返回的实际值为:%s；请求预期值为: %s。预期值与实际返回值相符!" % (text, data[0]["expect"]))
        self.log.info("-------test is pass--------")
        self.log.info("--------end--------")


if __name__ =="__main__":
    unittest.main()
