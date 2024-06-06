# 公共方法
# coding=utf-8
# 导入json库
import json
# 导入Template类
from string import Template
# 导入re库 即正则表达式的库
import re


# 根据参数匹配内容
def find(data):
    # 判断data类型是否为字典
    if isinstance(data, dict):
        # 对象格式化为str
        data = json.dumps(data)
        # 定义正则匹配规则 $ 和实际书写不一样，在程序中以\$表示，而反斜杠需要在前面再放置一个反斜杠
        pattern = "\\${(.*?)}"
        # 按匹配进行查询，把查询的结果返回
        return re.findall(pattern, data)


# 进行参数替换
def relace(ori_data, replace_data):
    # 对象格式化为str
    ori_data = json.dumps(ori_data)
    # 处理字符串的类，实例化并初始化原始字符
    s = Template(ori_data)
    # 使用新的字符，替换
    return s.safe_substitute(replace_data)


# 根据var，逐层获取json格式的值
def parse_relation(var, resdata):
    # 判断变量var是否存在
    if not var:
        # 不存在直接返回resdata内容
        return resdata
    else:
        # 存在则获取数组第1个内容
        resdata = resdata.get(var[0])
        # 从数组中删除第1个内容
        del var[0]
        # 递归
        return parse_relation(var, resdata)


# 测试代码
if __name__ == '__main__':
    ori_data = {"admin-token": "${token}"}
    replace_data = {'token': 'x015k878'}
    print(relace(ori_data, replace_data))
    red = find(
        {"id": "${id_name}", "editorType": "markdown", "title": "付出才能杰出", "alias": "${alias_name}", "thumbnail": None,
         "typeId": "1", "keywords": None, "digest": "<p>付出</p>", "canComment": False, "recommended": False,
         "privacy": False, "content": "<p>付出</p>\n", "markdown": "付出", "rubbish": False})
    print(red)
