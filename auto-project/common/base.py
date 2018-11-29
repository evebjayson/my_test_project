from common import cof
import random
import string
from common.HTTPservice import MyHttpservice

# def get_url(Route):
#     host = cof.get_host()
#     route = Route
#     url = "".join([host,route])
#     return url

def get_url(Route):
    '''拼接生成需要访问的url'''
    host = cof.get_host1()
    route = Route
    url = "".join([host,route])
    return url

def generate_username_str(randomlength=15):
    """
       创建随机用户名
       生成一个指定长度的随机字符串，其中
       string.digits=0123456789
       string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    username = "".join(str_list)
    return username

def generate_orderNo_deposit_str(randomlength):
    """
       创建随机存款订单号
       生成一个指定长度的随机字符串，其中
       string.digits=0123456789
       string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    orderNo = "".join(str_list)
    return orderNo

def generate_orderNo_withdrawal_str(randomlength):
    """
           创建随机取款订单号,为13位数字
           生成一个指定长度的随机字符串，其中
           string.digits=0123456789
        """
    str_list = [random.choice(string.digits) for i in range(randomlength)]
    orderNo = "".join(str_list)
    return orderNo

def get_response(url,Method,**kwargs):
    if Method == "get":
       pass
    if Method == "post":
        resp = MyHttpservice().post(url, **kwargs)
    if Method =="delete":
        pass
    if Method =="put":
        pass
    return resp


