import requests
from java_auto_web.common import base
from java_auto_web.data.readexcel import ExcelUtil



data = ExcelUtil("login").dict_data()
class login(object):
    def get_token(self):
        '''获取登陆token'''
        route = data[0]["route"]
        url = "".join(base.get_url(route))
        kwargs = {"json":eval(data[0]["data"]),"headers":eval(data[0]["header"])}
        token = requests.post(url,**kwargs).json()["token"]
        return token

