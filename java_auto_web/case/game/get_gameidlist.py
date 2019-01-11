from java_auto_web.common import base
from java_auto_web.data.readexcel import ExcelUtil

data = ExcelUtil("game").dict_data()
class GetGameIdList(object):
    """
    获取所有平台下面的一款游戏，来进行跳转
    并判断中心钱包的余额有没有带入到游戏中
    """
    def get_catDepotList(self):
        """
        获取真人，体育，棋牌，彩票平台的游戏id和name
        :return:
        """
        gameid_list = []
        depotname_list = []
        route = data[0]["route"]
        parameters = data[0]["parameters"]
        parameters = eval(parameters)
        for parameter in parameters:
            url = "".join(base.get_url(route) + "?" + "catId=" + str(parameter))
            header = eval(data[0]["header"])
            kwargs = {"headers": header}
            method = data[0]["method"]
            resp = base.get_response(url,method,**kwargs)
            catDepots = resp.json()["catDepots"]
            for catDepot in catDepots:
                gameid_list.append(catDepot["id"])
                depotname_list.append(catDepot["depotName"])
                new_dict = dict(zip(depotname_list,gameid_list))
        return new_dict

    def get_elecDepotList(self):
        """
        获取电子平台id和name
        :return:
        """
        id_list = []
        depotname_list = []
        route = data[1]["route"]
        url = base.get_url(route)
        header = eval(data[1]["header"])
        kwargs = {"headers":header}
        method = data[1]["method"]
        resp = base.get_response(url,method,**kwargs)
        tGmDepots = resp.json()["tGmDepots"]
        for tGmDepot in tGmDepots:
            id_list.append(tGmDepot["id"])
            depotname_list.append(tGmDepot["depotName"])
            new_dict = dict(zip(depotname_list,id_list))

        # 获取每个平台下面对应的具体游戏，后期会用random()方法来随机选择游戏
        gameid_list = []
        route = data[3]["route"]
        for v in new_dict.values():
            url = "".join(base.get_url(route) + data[3]["parameters"] + str(v))
            header = eval(data[3]["header"])
            kwargs = {"headers": header}
            method = data[3]["method"]
            resp = base.get_response(url, method, **kwargs)
            gameids = resp.json()["page"]["list"][0]["id"]
            gameid_list.append(gameids)
            new_slot_dict = dict(zip(depotname_list,gameid_list))
        return new_slot_dict

    def get_gameFishList(self):
        """
        获取捕鱼平台的游戏id和name
        :return:
        """
        id_list = []
        gameName_list = []
        route = data[2]["route"]
        url = "".join(base.get_url(route) + data[2]["parameters"])
        header = eval(data[2]["header"])
        kwargs = {"headers": header}
        method = data[2]["method"]
        resp = base.get_response(url, method, **kwargs)
        gamelist = resp.json()["page"]["list"]
        for game in gamelist:
            id_list.append(game["id"])
            gameName_list.append(game["gameName"])
            new_fish_dict = dict(zip(gameName_list,id_list))
        return new_fish_dict

    def dict_merge(self):
        """
        合并字典，游戏跳转中会用到
        :return:
        """
        new_dict = GetGameIdList().get_catDepotList()
        new_slot_dict = GetGameIdList().get_elecDepotList()
        new_fish_dict = GetGameIdList().get_gameFishList()
        d = dict(new_dict,**new_slot_dict,**new_fish_dict)
        return d


