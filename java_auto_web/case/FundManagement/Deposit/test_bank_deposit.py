import unittest
from java_auto_web.case.FundManagement.Deposit.get_deposit_cards import *
from java_auto_web.common import logger
from java_auto_web.data.readexcel import ExcelUtil

data = ExcelUtil("FundManagement").dict_data()
class BankDeposit(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_bank_deposit(self):
        '''会员使用银行转账进行存款'''
        route = data[5]["route"]
        url = "".join(base.get_url(route) +"?" + login_token.login().get_token())
        header = eval(data[5]["header"])
        header["token"] = login_token.login().get_token()
        for k in GetDepositChannel().get_deposit_cards()[0].keys():
            depositId = k
        for v in GetDepositChannel().get_deposit_cards()[0].values():
            fee = v
        json = {"depositId":"%s" %depositId,
                "fee":"%s" %fee}
        kwargs = {"headers":header,"json":json}
        method = data[5]["method"]

        resp = base.get_response(url,method,**kwargs)

        pass