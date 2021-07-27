import requests
import os
from api.admin_web import Adminweb

class Appusertest(Adminweb):

    def select_orglist(self, token,**kwargs):
        """机构选择"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/select/orgList'
        r = requests.post(url=url, headers=headers,json=data)
        self.format(r)
        return r.json()

    def appUser_info(self, token, **kwargs):
        """用户信息"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + 'appUser/info'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def employee_list(self, token, **kwargs):
        """从业人员信息"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/employee/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()



    def guest_list(self, token, **kwargs):
        """旅客信息列表"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/guest/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def guest_detail(self, token, **kwargs):
        """旅客信息详情"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/guest/detail'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def guest_roommates(self, token, **kwargs):
        """旅客信息同住人"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/guest/roommates'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()
