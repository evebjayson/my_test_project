import unittest
from java_auto_web.common import base,login_token,logger
from java_auto_web.case.game.get_gameidlist import *
from java_auto_web.case.FundManagement.Transfer import test_recoverbalance
from java_auto_web.data.readexcel import ExcelUtil

data1 = ExcelUtil("game").dict_data()
data2 = ExcelUtil("FundManagement").dict_data()
data3 = ExcelUtil("PersonalCenter").dict_data()
class GameJump(unittest.TestCase):
    def setUp(self):
        self.new_dict = GetGameIdList().dict_merge()
        self.log = logger.Log()
        self.len = len(self.new_dict)
        """
        游戏跳转
        :return:
        """
    def recoverBalance(self):
        route = data2[3]["route"]
        url = "".join(base.get_url(route) + "?" + login_token.login().get_token())
        header = eval(data2[3]["header"])
        header["token"] = login_token.login().get_token()
        kwargs = {"headers": header}
        method = data2[3]["method"]
        resp = base.get_response(url,method,**kwargs)
        return resp.json()

    def userinfo(self):
        route = data3[6]["route"]
        url = "".join(base.get_url(route) + data3[6]["parameters"] + login_token.login().get_token())
        header = eval(data3[6]["header"])
        kwargs = {"headers":header}
        method = data3[6]["method"]
        resp = base.get_response(url,method,**kwargs)
        user_balance = resp.json()["userInfo"]["balance"]
        return user_balance


    def test_transfer(self):
        '''转账'''
        route = data1[4]["route"]
        for gameid in self.new_dict.values():
            url = "".join(
                        base.get_url(route) + "?" + login_token.login().get_token() + data1[4]["parameters"] + str(gameid))
        recoverBalance_resp = GameJump().recoverBalance()  # 先将所有的平台余额回收到中心钱包
        header = eval(data1[4]["header"])
        header["token"] = login_token.login().get_token()
        kwargs = {"headers": header}
        method = data1[4]["method"]
        resp = base.get_response(url,method,**kwargs)
        depotname = list(self.new_dict)
        self.log.info("----------test start----------")
        self.log.info("请求内容为: %s" %kwargs)
        if GameJump().userinfo() == 0:
            self.log.info("会员转账成功平台有: %s" % depotname)
        elif GameJump().userinfo() != 0:
            depotId = recoverBalance_resp.json()["msg"]
            self.log.info("由于%s平台在维护或者已锁定，无法进行转账，请检查！" %depotId)
        else:
            pass
        self.log.info("----------test pass----------")
        self.log.info("----------test end----------")
if __name__ == "__main__":
    unittest.main()

