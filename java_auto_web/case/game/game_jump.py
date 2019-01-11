from java_auto_web.common import base,login_token,logger
from java_auto_web.case.game.get_gameidlist import *
from java_auto_web.data.readexcel import ExcelUtil

data = ExcelUtil("game").dict_data()
class GameJump(object):
    def __init__(self):
        self.new_dict = GetGameIdList().dict_merge()
        self.log = logger.Log()
        """
        游戏跳转
        :return:
        """
    def game_jump(self):
        route = data[4]["route"]
        for gameid in self.new_dict.values():
            url = "".join(base.get_url(route) + "?" + login_token.login().get_token() + data[4]["parameters"] + str(gameid) )
            header = eval(data[4]["header"])
            header["token"] = login_token.login().get_token()
            kwargs = {"headers":header}
            method = data[4]["method"]
            resp = base.get_response(url,method,**kwargs)
            self.log.info("----------test start----------")
            self.log.info("请求内容为: %s" %kwargs)
            self.log.info("响应内容为: %s" %resp.json())
        return resp
