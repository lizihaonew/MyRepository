# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_response_data
import unittest
import pytest
from nose.plugins.attrib import attr


@attr('external')
class DepartmentBaseSearch(WBSAPIBaseTestMixin):
    expected_response_format = {
        "success": bool,
        "msg": unicode,
    }

    @check_response_data
    def test_check_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    # 字符串拼接的中文不用+ u
    # 字符串拼接中文不用强制转换str
    # '"name":"' + cls.employee['name'] + '",' \
    @classmethod
    def setUpClass(cls):
        # 先查询
        cls.view_url = 'department/search.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{"entId":1}}'
        super(DepartmentBaseSearch, cls).setUpClass()

        cls.departmentcode = cls.response['data']['data']['list'][0]['code']
        cls.departmentname = cls.response['data']['data']['list'][0]['name']


@pytest.mark.externalapi
class DepartmentSearchByCodeTest(DepartmentBaseSearch, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(DepartmentSearchByCodeTest, cls).setUpClass()

        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{"entId":1,"code":"' + str(cls.departmentcode[0:2]) + '"}}'
        super(DepartmentSearchByCodeTest, cls).setUpClass()


@pytest.mark.externalapi
class DepartmentSearchByNameTest(DepartmentBaseSearch, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #FIXME name 不能使用中文
        cls.view_url = 'department/search.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{"entId":1,"name":"1"}}'
        super(DepartmentSearchByNameTest, cls).setUpClass()