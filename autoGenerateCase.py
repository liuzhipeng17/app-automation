# 需求:动态向unittestcase添加用例函数
# 利用闭包函数，返回是一个函数对象
import unittest
import xlrd
import importlib

def test_template(**value): 
    # 这个self可不能少, 因为Unittestcase里面的函数，至少有一个self
    def func(self):
        for k, v in value.items():
            print('{0}:{1}'.format(k,v))
    
    return func
    
class MyTestCase(unittest.TestCase):
    pass

arglists = [{'id':1, 'class':'my', 'name':'01'},{'id':2, 'class':'you', 'name':'02'}]
def _add_test(data_list):
    idx, len_data = 0, len(data_list)
    for data_json in data_list:
        setattr(MyTestCase, 'test_case_{0}_{1}'.format(len_data, idx), test_template(**data_json))
        idx = idx + 1

_add_test(arglists)

if __name__ =='__main__':
    unittest.main()
    
