#coding=utf-8
#使用TestLoader该类根据各种标准负责加载测试用例
import unittest
def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='E:\selenium_class\chapter7-5\project'
    #定义 discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,
                                                 pattern ='test*.py',
                                                 top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        print (testunit)
        for test_case in test_suite:
            testunit.addTests(test_case)

    return testunit
if __name__ == '__main__':
    alltestnames=creatsuite()
    runner =unittest.TextTestRunner()
    runner.run(alltestnames)
