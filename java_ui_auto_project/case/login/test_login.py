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
        url = base.get_url(data[1]["route"])
        self.driver.get(url)
        try:
            self.driver.find_element_by_xpath(eval(data[1]["Xpath"])["用户名输入"]).send_keys(eval(data[1]["params"])["username"])
            time.sleep(2)
            self.driver.find_element_by_xpath(eval(data[1]["Xpath"])["密码输入"]).send_keys(eval(data[1]["params"])["password"])
            time.sleep(2)
            self.driver.find_element_by_xpath(eval(data[1]["Xpath"])["登陆按钮"]).click()
        except Exception as e:
            self.log.error("错误的参数:".format(e))
        time.sleep(3)
        text = self.driver.find_element_by_xpath(eval(data[1]["Xpath"])["查找元素"]).text
        self.log.info("--------start--------")
        self.log.info("返回的实际值为: %s ;请求预期值为: %s。预期值与实际返回值相符!" % (text, data[1]["expect"]))
        self.assertEqual(data[1]["expect"],text,msg="失败原因:期望值:%s not same 实际值:%s" % (data[1]["expect"], text))
        print("返回的实际值为: %s ;请求预期值为: %s。预期值与实际返回值相符!" % (text, data[1]["expect"]))
        self.log.info("-------test is pass--------")
        self.log.info("--------end--------")


if __name__ =="__main__":
    unittest.main()
