# -*- coding: UTF-8 -*-

import unittest
from HTMLTestRunner import HTMLTestRunner
from unittest.suite import TestSuite
import os
import time
from tools.send_msg import MSG

base_path = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), 'SYProject'))
case_path = os.path.join(base_path, 'src', 'testcase')
report_path = os.path.join(base_path, 'report')
print(report_path)


class Run_All:
    @staticmethod
    def run_test():
        msg = MSG()
        suites = TestSuite()
        now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
        discover = unittest.defaultTestLoader.discover('./src/testcase',
                                                       pattern="test*.py")
        print(discover)
        # for root, dirs, files in os.walk(case_path):
        #     pass
        # for d in dirs:
        #     if d != '__pycache__':
        #         discovers = unittest.defaultTestLoader.discover(d, pattern="test*.py")
        #         suites.addTest(discovers)
        #     else:
        #         continue

        suites.addTest(discover)
        with open(f'{report_path}\Report_{now}.html', 'wb') as f:
            runner = HTMLTestRunner(stream=f,
                                    title=u'接口测试报告',
                                    description=u'测试用例的执行情况',
                                    verbosity=2)
            runner.run(suites)


    # suite = unittest.TestSuite()
    # 使用这种方法可以对测试用例排序
    # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    # suite.addTests(tests)

    # 使用TestLoader的方法传入TestCase
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testcase.Test_Case))

    # 在同目录下生成txt格式的测试报告
    # with open('UnittestTextReport.txt', 'a') as f:
    # runner = unittest.TextTestRunner(stream=f, verbosity=2)
    # runner.run(suite)

    # with open(report_path, 'wb') as f:
    #     runner = HTMLTestRunner(stream=f,
    #                             title=u'测试报告',
    #                             description=u'测试用例的执行情况',
    #                             verbosity=2)
    #     runner.run(suite)


if __name__ == '__main__':
    ra = Run_All()
    ra.run_test()
