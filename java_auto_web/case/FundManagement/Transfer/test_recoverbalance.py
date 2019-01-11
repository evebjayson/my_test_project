import unittest
from java_auto_web.common import logger,login_token,base
from java_auto_web.data.readexcel import ExcelUtil

data = ExcelUtil("FundManagement").dict_data()
class CheckBalance(unittest.TestCase):
    """
    先获取所有的游戏平台，通过id查询每个平台的余额，
    如果所有的平台都不足以转账，则不执行，一键回中心接口
    :return:
    """
    def setUp(self):
        self.log = logger.Log()

    def get_platformID(self):
        """
        获取所有平台id，写入到空列表
        :return:
        """
        route = data[1]["route"]
        url = "".join(base.get_url(route) + "?" + login_token.login().get_token())
        header = eval(data[1]["header"])
        header["token"] = login_token.login().get_token()
        kwargs = {"headers": header}
        method = data[1]["method"]
        resp = base.get_response(url, method, **kwargs)

        # 遍历所有的平台id到一个列表中
        tGmDepots = resp.json()["tGmDepots"]
        id_list = []
        for tGmDepot in tGmDepots:
            id = tGmDepot['id']
            id_list.append(id)
        return id_list

    def get_platform_balances(self):
        """
        获取所有平台余额，写入一个空列表
        :return:
        """
        route = data[2]["route"]
        id_list = CheckBalance().get_platformID()
        balance_list = []
        for id in id_list:
            id = str(id)
            url = "".join(base.get_url(route) + "?" + login_token.login().get_token()) + data[2]["parameters"] + id
            header = eval(data[2]["header"])
            header["token"] = login_token.login().get_token()
            kwargs = {"headers": header}
            method = data[2]["method"]
            resp = base.get_response(url, method, **kwargs)
            balances = resp.json()["data"]["balance"]
            balance_list.append(balances)
        return balance_list
    def dict_merge(self):
        """
         #将两个列表合并成一个字典，在下面判断一键回中心时，平台余额，输出符合的平台
        :return:
        """
        balance_list = CheckBalance().get_platform_balances()
        id_list = CheckBalance().get_platformID()
        new_dict = dict(zip(id_list, balance_list))
        return new_dict

    def test_recoverbalance(self):
        """
        一键回中心
        判断：
        1.如果所有平台余额小于1，则一键回中心失败
        2.如果有平台为锁定状态，则一键回中心失败
        3.如果有平台是维护状态，则一键回中心失败
        isSign：
            0：表示维护状态，1：表示锁定状态
        :return:
        """
        new_dict = CheckBalance().dict_merge()
        new_id_list = [] # 定义一个空列表存放符合转账的平台id

        route = data[3]["route"]
        url = "".join(base.get_url(route) + "?" + login_token.login().get_token())
        header = eval(data[3]["header"])
        header["token"] = login_token.login().get_token()
        kwargs = {"headers": header}
        method = data[3]["method"]

        for balance in new_dict.values():
            if balance > 1 or balance == 1:
                id = list(new_dict.keys())[list(new_dict.values()).index(balance)]
                new_id_list.append(id)
        self.log.info("所有平台余额为: %s,平台余额符合一键回中心的平台有: %s" % (new_dict, new_id_list))
        resp = base.get_response(url, method, **kwargs)
        self.log.info("----------test start----------")
        self.log.info("请求内容为: %s" % kwargs)
        self.log.info("响应内容为: %s" % resp.json())
            # if '1' or '0' in resp.json()["isSign"]:
            #     self.assertEqual(501, resp.json()["code"], msg="失败原因: %s != %s" % (501, resp.json()["code"]))
            #     self.log.info("有平台为锁定状态或者为维护状态，一键回中心失败,请检查所有平台的状态!")
            # else:
        self.assertEqual(501, resp.json()["code"], msg="失败原因: %s != %s" % (501, resp.json()["code"]))
        self.log.info("----------test end----------")
if __name__ == "__main__":
    unittest.main()
