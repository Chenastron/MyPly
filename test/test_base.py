# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/16 17:07"

test_dict = {
    'a': 0
}

a = test_dict.get('b', 'default')
b = test_dict['c'] = 0
print(b, test_dict['c'])
