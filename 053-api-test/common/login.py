import requests
from common import base
from common.logger import Log

s = requests.Session()
class login(object):

    def __init__(self):
        self.log = Log()
    def login_session(self):
        '''获取登陆session'''
        route = "/home/dologin"
        url = "".join([base.get_url(route)])
        json = {"username": "jayson",
                "password": "Admin888***"}

        kwargs = {"json": json}
        Method = "post"

        requests.post(url,Method,**kwargs)
        return s


class dologin():

    s = login().login_session()
    def Login(self):
        params = {"_": 1542246127072
                }
        url = "http://at-e053-demo.e-veb.info/Member/List"
        resp = s.get(url,params=params)
        print(resp.text)
dologin().Login()