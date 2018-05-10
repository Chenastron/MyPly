# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 21:07"

from interpreter.outputRes import OutputRes

file_choice = 2
file_path = 'sub_test' if file_choice == 1 else 'test_code.py'
# 从文件读入要执行的代码, 也可以直接写字符串
with open(file_path, 'r') as f:
    data = f.read()

output_res = OutputRes(data)
res = output_res.get_res()

# 输出相应的值
# print(res['lex'])
# print(res['yacc'])
# print(res['exe'])
