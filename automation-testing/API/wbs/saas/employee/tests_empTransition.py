# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import time
import pytest
from nose.plugins.attrib import attr
from API.wbs import execute_mysql


@attr('issues')
#@attr('internal')
#@attr('external')
class EmpTransitionTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'employee/empTransition.json'

    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    valid_time = time.strftime('%Y-%m-%d', time.localtime(time.time()+86400))

    @classmethod
    def clear_transition_record(cls):
        inst = execute_mysql.ExecuteMysql()
        cls.result = inst.execute_select_sql('select * from emp_transition where empId="322";')
        if cls.result:
            inst.execute_delete_sql('delete from emp_transition where empId="322";')

    @check_response_data
    def test_response_with_successful_workflow(self):
        self.maxDiff = None
        # self.response = self.do_request(self.data)
        self.expected_response = {
            "success": True,
            "msg": u'操作成功',
            "errorCode": None
        }

    @classmethod
    def setUpClass(cls):
        cls.clear_transition_record()

        cls.data = 'data={' \
                   '"token":'+ cls.generate_token() + ',' \
                   '"param":{' \
                   '"empId":"322",' \
                   '"deptId":"7",' \
                   '"effectDate":"' + cls.valid_time + '"'\
                   '},"sign":"354d13a6f4f2e8ff58a5d93a757c1bae"}'
        super(EmpTransitionTest, cls).setUpClass()


@pytest.mark.issues
#@pytest.mark.externalapi
class EmpTransitionAbnormalTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'employee/empTransition.json'

    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    @check_response_data
    def test_response_with_date_error(self):
        self.maxDiff = None
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"异动生效日期应大于系统当前日期！",
            "errorCode": None,
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={' \
                   '"token":' + cls.generate_token() + ',' \
                   '"param":{' \
                   '"empId":"138",' \
                   '"deptId": "7",' \
                   '"effectDate":"2017-08-3"' \
                   '},' \
                   '"sign":"354d13a6f4f2e8ff58a5d93a757c1bae"' \
                   '}'
        super(EmpTransitionAbnormalTest, cls).setUpClass()

