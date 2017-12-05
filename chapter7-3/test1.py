#coding=utf-8
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        number = input("Enter a number:")
        self.number = int(number)
    def test_case(self):
        #msg 是否可选有参数，用于定义测试失败所要提示的信息
        self.assertEqual(self.number, 10, msg="You input is not 10!")
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()
