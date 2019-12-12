# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest,time
from API.wbs import execute_mysql

class BatchEmpTransitionTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/employee/batchEmpTransition.json'

    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    valid_time = time.strftime('%Y-%m-%d', time.localtime(time.time()+86400))

    @classmethod
    def clear_transition_record(cls):
        inst = execute_mysql.ExecuteMysql()
        cls.result = inst.execute_select_sql("SELECT * FROM emp_transition WHERE empId IN ('336', '337');")
        if cls.result:
            inst.execute_delete_sql("DELETE FROM emp_transition WHERE empId IN ('336', '337');")

    @check_all_response_data
    def test_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
            "data": [
            {
                "mobile": "15100000025",
                "success": True,
                "msg": None
            },
            {
                  "mobile": "15100000026",
                  "success": True,
                  "msg": None
            }
            ]
        }

    @classmethod
    def setUpClass(cls):
        cls.clear_transition_record()
        cls.data = 'data={' \
                   '"token":' + cls.generate_token() + ',' \
                   '"param":[{' \
                   '"empId":"336",' \
                   '"deptId": "5",' \
                   '"effectDate":"' + cls.valid_time + '"' \
                   '},{' \
                   '"empId":"337",' \
                   '"deptId": "5",' \
                   '"effectDate":"' + cls.valid_time + '"' \
                   '}],"sign":"354d13a6f4f2e8ff58a5d93a757c1bae"}'
        super(BatchEmpTransitionTest, cls).setUpClass()





class BatchEmpTransitionAbnormalTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/employee/batchEmpTransition.json'

    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    @check_all_response_data
    def test_response_with_date_error(self):
        self.maxDiff = None
        self.expected_response = {
            "success": False,
            "msg": u"批量员工异动失败！",
            "errorCode": None,
            "data":
                [
                {
                    "mobile": None,
                    "success": False,
                    "msg": u"异动生效日期应大于系统当前日期！"
                },
                {
                    "mobile": None,
                    "success": False,
                    "msg": u"异动生效日期应大于系统当前日期！"
                }
            ]
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={' \
                   '"token": ' + cls.generate_token() + ',' \
                   '"param": [{' \
                   '"empId": "138",' \
                   '"deptId": "6",' \
                   '"effectDate": "2017-08-13"' \
                   '},{' \
                   '"empId": "137",' \
                   '"deptId": "6",' \
                   '"effectDate": "2017-08-13"' \
                   '}],"sign": "354d13a6f4f2e8ff58a5d93a757c1bae"}'
        super(BatchEmpTransitionAbnormalTest, cls).setUpClass()


