import requests
from common import base
from data.readexcel import ExcelUtil


data = ExcelUtil("login").dict_data()

class login(object):


    # def get_session(self):
    #     '''取登陆session'''
    #     route = data[0]["route"]
    #     url = "".join(base.get_url(route))
    #     kwargs = {"json": json.loads(data[0]["data"]), "headers": eval(data[0]["header"])}
    #     s.post(url,**kwargs)
    #     self.log.info("获取的session:%s"%s)
    #     return s

    def get_token(self):
        '''取登陆token'''
        route = data[0]["route"]
        url = "".join(base.get_url(route))
        kwargs = {"json": eval(data[0]["data"]), "headers": eval(data[0]["header"])}
        token = requests.post(url, **kwargs).json()["token"]
        return token


