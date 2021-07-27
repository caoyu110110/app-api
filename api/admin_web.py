import requests

from api.baseapi import BaseApi

class Adminweb(BaseApi):
    # host地址
    # 演示（预发布）环境地址
    ucenter_host = 'http://172.26.236.70:701//prod-api/'
    test_user_1 = {'username':'admin', 'password':'Cqbg@hdsP@)@!1'}

   # 获取验证码URL
   #  captchaImage_url= ucenter_host + '/captchaImage'
   # 登录URL
    login_url = ucenter_host + '/login'
    Content_Type = 'application/json'

    # token
    token = dict()
    # def captchaImage(cls):
    #     """
    #     验证码
    #     :param user:
    #     :return:
    #     """
    #     captchaImage_code = requests.get(url=cls.captchaImage_url)
    #
    #     return captchaImage_code.json()

    def login(cls, user=1):
        """
        登录
        :param user:
        :return:
        """
        username = ''
        password = ''
        if user == 1:

            username = cls.test_user_1['username']
            password = cls.test_user_1['password']

        else:
            print('参数错误')

        r =requests.post(url=cls.login_url,
                         headers={'Content-Type':cls.Content_Type},
                         json={'username':username, 'password':password}
                         )
        return r.json()


    def get_token(cls):
        """
        获取token
        :return:
        """
        token = cls.login()['token']
        return token

A = Adminweb()
# 打印登录的token
# print(A.get_token())