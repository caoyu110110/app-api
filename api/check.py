import requests
import os
from api.admin_web import Adminweb

class Check(Adminweb):

    def check_recordList(self, token, **kwargs):
        """核查记录列表"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/check/recordList'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()


    def statistics(self, token, **kwargs):
        """未核查、未处理警情统计"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/app/statistics'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def roomCheck_list(self, token, **kwargs):
        """查询未核查房屋列表"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/roomCheck/list'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def roomCheck_insert(self, token, **kwargs):
        """查询未核查房屋列表"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/roomCheck/insert'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def roomCheck_uploadCheckPhoto(self, token, **kwargs):
        """新增房屋核查/检查-上传图片"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/roomCheck/uploadCheckPhoto'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def roomCheck_detail(self, token, **kwargs):
        """房屋核查详情页"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/server/roomCheck/detail'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

