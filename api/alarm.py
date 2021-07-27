import requests
import os
from api.admin_web import Adminweb

class Alarm(Adminweb):

    def alarm_alarmList(self, token, **kwargs):
        """警情信息列表"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/alarm/alarmList'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def alarm_alarmDetail(self, token, **kwargs):
        """警情信息详情"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/alarm/alarmDetail'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def alarm_handleDetail(self, token, **kwargs):
        """警情处理详情"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/alarm/handleDetail'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def alarmHandle_uploadAlarmPhoto(self, token, **kwargs):
        """警情处理-上传图片"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/alarmHandle/uploadAlarmPhoto'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def alarmHandle_insertHandle(self, token, **kwargs):
        """新增警情"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/alarmHandle/insertHandle'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def alarmHandle_revokeHandle(self, token, **kwargs):
        """警情处理-重新处理"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/alarmHandle/revokeHandle'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()

    def alarmHandle_invalidHandle(self, token, **kwargs):
        """无效警情"""
        headers = {

            "Content-Type": Adminweb.Content_Type,
            "Authorization": token
        }
        data = {}
        data.update(kwargs)
        url = Adminweb.ucenter_host + '/appserver/alarmHandle/invalidHandle'
        r = requests.post(url=url, headers=headers, json=data)
        self.format(r)
        return r.json()
