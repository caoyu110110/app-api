import pytest
import allure
from api.baseapi import BaseApi
from api.alarm import Alarm
import api.admin_web

allure.feature("警情相关信息接口模块")
class Testalarm:

    data = BaseApi.yaml_load('../yaml_data/test_alarm.yaml')

    def setup(self):
        self.adminweb = api.admin_web.Adminweb()
        self.alarm = Alarm()

    @pytest.mark.parametrize('data', data['test_alarm_alarmList'])
    def test_alarm_alarmList(self, data):
        """
        警情信息列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.alarm.alarm_alarmList(token=token, authorization=token, param=data['param'],
                                         pageNum=data['param']['pageNum'], pageSize=data['param']['pageSize'],
                                         handleType=data['param']['handleType'], alarmType=data['param']['alarmType'])
        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_alarm_alarmDetail'])
    def test_alarm_alarmDetail(self, data):
        """
        警情信息详情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.alarm.alarm_alarmDetail(token=token, authorization=token, param=data['param'],
                                           alarmIidd=data['param']['alarmIidd'], alarmType=data['param']['alarmType'],
                                           alarmDetailType=data['param']['alarmDetailType'])
        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_alarmHandle_uploadAlarmPhoto'])
    def test_alarmHandle_uploadAlarmPhoto(self, data):
        """
        警情处理-上传图片
        :return:
        """
        token = self.adminweb.get_token()
        r = self.alarm.alarmHandle_uploadAlarmPhoto(token=token, authorization=token, param=data['param'],
                                                      alarmIidd=data['param']['alarmIidd'],
                                                      alarmPhoto=data['param']['alarmPhoto'])
        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_alarmHandle_insertHandle'])
    def test_alarmHandle_insertHandle(self, data):
        """
        新增警情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.alarm.alarmHandle_insertHandle(token=token, authorization=token, param=data['param'],
                                                  alarmIidd=data['param']['alarmIidd'],
                                                  alarmType=data['param']['alarmType'],
                                                  handleTime=data['param']['handleTime'],
                                                  writeTime=data['param']['writeTime'],
                                                  handleContext=data['param']['handleContext'],
                                                  captureType=data['param']['captureType'],
                                                  imgList=data['param']['imgList'])
        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_alarmHandle_revokeHandle'])
    def test_alarmHandle_revokeHandle(self, data):
        """
       警情处理-重新处理
        :return:
        """
        token = self.adminweb.get_token()
        r = self.alarm.alarmHandle_revokeHandle(token=token, authorization=token, param=data['param'],
                                                  alarmIidd=data['param']['alarmIidd'], groupId=data['param']['groupId'])
        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_alarmHandle_invalidHandle'])
    def test_alarmHandle_invalidHandle(self, data):
        """
       警情处理-无效警情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.alarm.alarmHandle_invalidHandle(token=token, authorization=token, param=data['param'],
                                                   alarmIidd=data['param']['alarmIidd'], groupId=data['param']['groupId'])
        assert r['message'] == 'SUCCESS'
