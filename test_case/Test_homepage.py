import pytest
import allure
from api.baseapi import BaseApi
from api.homepage import Homepage
import api.admin_web

allure.feature("首页相关接口模块")
class Testhomepage:

    data = BaseApi.yaml_load('../yaml_data/test_homepage.yaml')

    def setup(self):
        self.adminweb = api.admin_web.Adminweb()
        self.homepage = Homepage()


    @pytest.mark.parametrize('data', data['test_homePage_appInfo'])
    def test_homePage_appInfo(self, data):
        """
        首页接口
        :return:
        """
        token = self.adminweb.get_token()
        r = self.homepage.homePage_appInfo(token=token, authorization=token, param=data['param'],
                                           dateTime=data['param']['dateTime'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_homePage_appInfo'])
    def homePage_guestResource(self, data):
        """
        首页旅客来源列表接口
        :return:
        """
        token = self.adminweb.get_token()
        r = self.homepage.homePage_guestResource(token=token, authorization=token, param=data['param'],
                                                 dateTime=data['param']['dateTime'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_homePage_passengerFlow'])
    def test_homePage_passengerFlow(self, data):
        """
        首页旅客流量列表接口
        :return:
        """
        token = self.adminweb.get_token()
        r = self.homepage.homePage_passengerFlow(token=token, authorization=token, param=data['param'],
                                                 dateTime=data['param']['dateTime'], choice=data['param']['choice'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_hotel_list'])
    def test_hotel_list(self, data):
        """
        门店列表接口
        :return:
        """
        token = self.adminweb.get_token()
        r = self.homepage.hotel_list(token=token, authorization=token, param=data['param'],
                                     hotelName=data['param']['hotelName'], roomName=data['param']['roomName'],
                                     merchantName=data['param']['merchantName'], pageSize=data['param']['pageSize'],
                                     pageNum=data['param']['pageNum']
                                     )
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_hotel_hotelDetail'])
    def test_hotel_list(self, data):
        """
        门店详情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.homepage.hotel_hotelDetail(token=token, authorization=token, param=data['param'],
                                            hotelCode=data['param']['hotelCode'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_room_list'])
    def test_room_list(self, data):
        """
        房屋列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.homepage.room_list(token=token, authorization=token, param=data['param'],
                                    roomName=data['param']['roomName'], roomAddress=data['param']['roomAddress'],
                                    merchantName=data['param']['merchantName'],
                                    appIsMyTurnout=data['param']['appIsMyTurnout'],
                                    pageNum=data['param']['pageNum'], pageSize=data['param']['pageSize'])

        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_room_Detail'])
    def test_room_Detail(self, data):
        """
        房屋详情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.homepage.room_Detail(token=token, authorization=token, param=data['param'],
                                      roomCode=data['param']['roomCode'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_room_update'])
    def test_room_update(self, data):
        """
        编辑房屋
        :return:
        """
        token = self.adminweb.get_token()
        r = self.homepage.room_update(token=token, authorization=token, param=data['param'],
                                      roomCode=data['param']['roomCode'], building=data['param']['building'],
                                      unit=data['param']['unit'], floor=data['param']['floor'],
                                      buildingName=data['param']['buildingName'],
                                      psbUnitCode=data['param']['psbUnitCode'],
                                      turnoutCode=data['param']['turnoutCode'], bedNum=data['param']['bedNum'],
                                      isOpen=data['param']['isOpen'], roomName=data['param']['roomName'],
                                      iidd=data['param']['iidd'], images=data['param']['images'])
        assert r['message'] == 'SUCCESS'
