import pytest
import allure
from api.baseapi import BaseApi
from api.appuser import Appusertest
import api.admin_web


@allure.feature('个人中心模块接口')
class Testappuser:

    data = BaseApi.yaml_load('../yaml_data/test_appuser.yaml')

    def setup(self):
        self.adminweb = api.admin_web.Adminweb()
        self.apptest = Appusertest()

    @allure.story('用户名、密码正确，登录成功')
    @allure.step('测试用户登录后的信息是否正确')
    # Allure中对严重级别的定义：
    # blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
    # critical级别：临界缺陷（ 功能点缺失）
    # normal级别：普通缺陷（数值计算错误）
    # minor级别：次要缺陷（界面错误与UI需求不符）
    # trivial级别：轻微缺陷（必输项无提示，或者提示不规范）

    # 使用方法：
    # @allure.severity(allure.severity_level.CRITICAL)
    # 或者 @ allure.severity('critical')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('data', data['test_statistics'])
    def test_statistics(self,data):
        token = self.adminweb.get_token()
        r = self.apptest.appUser_info(token=token, authorization=token,param=data['param'])

        assert r['message'] == 'SUCCESS'

    @allure.step('测试机构选择下拉列表框数据是否正确')
    def test_select_orglist(self):
        """
        机构选择
        :return:
        """
        token = self.adminweb.get_token()
        r = self.apptest.select_orglist(token=token, authorization=token)
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_employee_list'])
    def test_statistics(self,data):
        """
        从业人员信息
        :return:
        """
        token = self.adminweb.get_token()
        r = self.apptest.employee_list(token=token, authorization=token,param=data['param'],employeeName=data['param']['employeeName'], pageSize=data['param']['pageSize'],
                                          pageNum=data['param']['pageNum'],employeeCardNum=data['param']['employeeCardNum'])
        assert r['message'] == 'SUCCESS'


    @pytest.mark.parametrize('data', data['test_guest_list'])
    def test_guest_list(self,data):
        """
       旅客信息列表
        :return:
        """
        token = self.adminweb.get_token()
        r = self.apptest.guest_list(token=token, authorization=token,param=data['param'], pageNum=data['param']['pageNum'], pageSize=data['param']['pageSize'],
                                    name=data['param']['name'], cardNum=data['param']['cardNum'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_guest_list'])
    def test_guest_list(self,data):
        """
       旅客信息详情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.apptest.guest_list(token=token, authorization=token,param=data['param'], cardNum=data['param']['cardNum'], name=data['param']['name'])
        assert r['message'] == 'SUCCESS'

    @pytest.mark.parametrize('data', data['test_guest_roommates'])
    def test_guest_roommates(self,data):
        """
       旅客信息详情
        :return:
        """
        token = self.adminweb.get_token()
        r = self.apptest.guest_roommates(token=token, authorization=token,param=data['param'], guestCode=data['param']['guestCode'])
        assert r['message'] == 'SUCCESS'

