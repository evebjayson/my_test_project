from java_auto_web.common import logger,login_token,base
from java_auto_web.data.readexcel import ExcelUtil

data = ExcelUtil("FundManagement").dict_data()
class GetDepositChannel(object):
    '''获取所有存款渠道'''
    def __init__(self):
        self.log = logger.Log()

    def get_deposit_cards(self):
        '''获取所有的银行卡支付信息'''
        cards_list = [] # 存放存款银行信息
        minAmout_list = [] # 存放银行卡存款最小值
        route = data[4]["route"]
        url = "".join(base.get_url(route) + data[4]["parameters"] + login_token.login().get_token())
        header = eval(data[4]["header"])
        header["token"] = login_token.login().get_token()
        kwargs = {"headers": header}
        method = data[4]["method"]
        resp = base.get_response(url, method, **kwargs)
        # self.log.info("请求参数为: %s" %kwargs)
        bank_cards = resp.json()["data"]["bankCards"]
        for bank_card in bank_cards:
            cards_list.append(bank_card["id"])
        for bank_minamout in bank_cards:
            minAmout_list.append(bank_minamout["minAmout"])
        new_dict = dict(zip(cards_list,minAmout_list))
        return new_dict,resp  # 返回一个银行id和最新存款的字典，存款会用到

