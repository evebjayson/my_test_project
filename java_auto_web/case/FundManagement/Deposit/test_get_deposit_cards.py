import unittest
from java_auto_web.case.FundManagement.Deposit.get_deposit_cards import *
from java_auto_web.common import logger
from java_auto_web.data.readexcel import ExcelUtil



data = ExcelUtil("FundManagement").dict_data()
class BankDepositCards(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_get_deposit_cards(self):
        '''获取存款银行信息'''
        resp = GetDepositChannel().get_deposit_cards()[1]
        self.log.info("----------test start----------")
        self.log.info("响应内容为: %s" %resp.text)
        self.assertIn(data[4]["expect"],resp.text,msg="失败原因: %s not in %s" %(data[4]["expect"],resp.text))
        self.log.info("--------test is pass--------")
        self.log.info("----------end----------")


if __name__ == "__main__":
    unittest.main()