from java_auto_web.common import cof
import random
import string
from java_auto_web.common.HTTPservice import MyHttpservice
from java_auto_web.common import login_token
from java_auto_web.data.readexcel import ExcelUtil



def get_url(Route):
    '''拼接生成需要访问的url'''
    host = cof.get_java_host()
    route = Route
    url = "".join([host,route])
    return url



def generate_username_str(randomlength):
    """
       创建随机用户名
       以字母开头，字母、数字组合
       生成一个指定长度的随机字符串，其中
       string.digits=0123456789
       string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits+string.ascii_letters) for i in range(randomlength)]
    random.shuffle(str_list)
    username = "".join([i for i in str_list])
    return username

def generate_password_str(randomlength):
    """
       创建随机密码
       生成一个指定长度的随机字符串，其中
       string.digits=0123456789
       string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    password = "".join(str_list)
    return password

def create_random_numbers(randomlength=6):
    '''创建一个六位数来生成注册验证码
        string.digits=0123456789
    '''
    str_list = [random.choice(string.digits) for i in range(randomlength)]
    numbers = "".join(str_list)
    numbers = "?" + "v=" + numbers
    return numbers

def create_random_address():
    '''支行名称'''
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


def create_bank_cardNo(randomlength):
    '''创建一个银行卡号
            string.digits=0123456789
        '''
    str_list = [random.choice(string.digits) for i in range(randomlength)]
    numbers = "".join(str_list)
    return numbers

import os
def read_random_bankname():
    '''随机读取bankname文件中的一个银行名称'''
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(os.path.dirname(path) + "\\config\\bankname")
    print(filepath)
    with open(filepath,'r',encoding='utf-8') as f:
        f = f.readlines()
        bankname = random.choice(f)
        return bankname


def read_random_provincename():
    '''随机读取一个省份名称'''
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(os.path.dirname(path) + "\\config\\provincesname")
    with open(filepath,'r',encoding='utf-8') as f:
        f = f.readlines()
        provincesname = eval(random.choice(f))
        provincename = provincesname[0]
        return provincename

def read_cityename():
    '''基于上面获取的省份名称匹配一个正确的城市名称'''
    pass
# def generate_orderNo_deposit_str(randomlength):
#     """
#        创建随机存款订单号
#        生成一个指定长度的随机字符串，其中
#        string.digits=0123456789
#        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#     """
#     str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
#     orderNo = "".join(str_list)
#     return orderNo

# def generate_orderNo_withdrawal_str(randomlength):
#     """
#            创建随机取款订单号,为13位数字
#            生成一个指定长度的随机字符串，其中
#            string.digits=0123456789
#         """
#     str_list = [random.choice(string.digits) for i in range(randomlength)]
#     orderNo = "".join(str_list)
#     return orderNo



def get_response(url,Method,**kwargs):
    if Method == "get":
       resp = MyHttpservice().get(url,**kwargs)
    if Method == "post":
        resp = MyHttpservice().post(url, **kwargs)
    if Method =="delete":
        pass
    if Method =="put":
        pass
    return resp





