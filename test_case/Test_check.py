import pytest
import allure
from api.baseapi import BaseApi
from api.check import Check
import api.admin_web

allure.feature("核查警情相关接口模块")
class Testcheck:

    data = BaseApi.yaml_load('../yaml_data/test_check.yaml')

    def setup(self):
        self.adminweb = api.admin_web.Adminweb()
        self.check = Check()

    @pytest.mark.parametrize('data', data['test_check_recordList'] )
    def test_check_recordList(self ,data):
        """
        未核查、未处理警情统计
        :return:
        """
        token = self.adminweb.get_token()
        r = self.check.check_recordList(token=token, authorization=token ,param=data['param']
                                          ,roomCode=data['param']['roomCode'], pageSize=data['param']['pageSize'],
                                          pageNum=data['param']['pageNum'])

        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_statistics'])
    def test_statistics(self ,data):
        """
        核查记录列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.check.statistics(token=token, authorization=token ,param=data['param'])

        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_roomCheck_list'])
    def test_roomCheck_list(self,data):
        """
        查询未核查房屋列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.check.roomCheck_list(token=token, authorization=token,param=data['param'], pageNum=data['param']['pageNum'],pageSize=data['param']['pageSize'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_roomCheck_insert'])
    def test_roomCheck_insert(self,data):
        """
        新增房屋核查/检查*
        :return:
        """
        token = self.adminweb.get_token()
        r = self.check.roomCheck_insert(token=token, authorization=token,param=data['param'], hotelCode=data['param']['hotelCode'],roomCode=data['param']['roomCode'],
                                          checkContent=data['param']['checkContent'],checkSituation=data['param']['checkSituation'],checkResult=data['param']['checkResult'],
                                          remark=data['param']['remark'],arriveTime=data['param']['arriveTime'],photoStr=data['param']['photoStr'])
        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_roomCheck_uploadCheckPhoto'])
    def test_roomCheck_uploadCheckPhoto(self,data):
        """
       新增房屋核查/检查-上传图片
        :return:
        """
        token = self.adminweb.get_token()
        r = self.check.roomCheck_uploadCheckPhoto(token=token, authorization=token,param=data['param'], roomCode=data['param']['roomCode'],photo=data['param']['photo'])
        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_roomCheck_detail'])
    def test_roomCheck_detail(self,data):
        """
        房屋核查详情页
        :return:
        """
        token = self.adminweb.get_token()
        r = self.check.roomCheck_detail(token=token, authorization=token,param=data['param'], roomCode=data['param']['roomCode'])
        assert r['message'] == 'SUCCESS'

