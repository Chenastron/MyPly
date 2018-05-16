import json
from django.http import HttpResponse
from django.views.generic import View

from utils.interpreter.outputRes import OutputRes


class IndexView(View):
    """负责将得到的字符串解析, 返回一个json有词法语法执行结果的三部分"""
    def post(self, request):
        # 目前规定的的key是string
        before_parse_string = request.POST['string']
        # 字符串解析的解释器
        interpreter_output = OutputRes(before_parse_string)
        # 得到结果
        res = interpreter_output.get_res()
        return HttpResponse(json.dumps(res), content_type='application/json')
