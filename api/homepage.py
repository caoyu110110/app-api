import requests
import os
from api.admin_web import Adminweb

class Homepage(Adminweb):


    def homePage_appInfo(self, token, **kwargs):
        """首页接口"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/homePage/appInfo'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def homePage_guestResource(self, token, **kwargs):
        """首页旅客来源列表接口"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/homePage/guestResource'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def homePage_passengerFlow(self, token, **kwargs):
        """首页旅客流量列表接口"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/homePage/passengerFlow'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def hotel_list(self, token, **kwargs):
        """门店列表接口"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/hotel/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def hotel_hotelDetail(self, token, **kwargs):
        """门店详情"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/hotel/hotelDetail'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def room_list(self, token, **kwargs):
        """房屋列表"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/app/room/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def room_Detail(self, token, **kwargs):
        """房屋详情"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/app/room/detail'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def room_update(self, token, **kwargs):
        """房屋编辑"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/app/room/update'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()
