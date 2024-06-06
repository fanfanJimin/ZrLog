# config层级 主要用于读取接口自动化测试用例中所需的各项配置信息和文件路径
# setting 复制存储配执行信息
# coding=utf-8
# 导入os库
import os

# 获取当前文件的绝对路径 相对路径为 real
abs_path = os.path.realpath(__file__)
# print("abs_path :" + abs_path)
# 获取根目录信息(本来是所在目录的文件夹，嵌套就是上一层级
project_path = os.path.dirname(os.path.dirname(abs_path))
# print("上一级目录：" + project_path)
# 通过os.sep（）,来获取config目录的全路径
_conf_path = project_path + os.sep + "config"
# print("conf: " + _conf_path )
_log_path = project_path + os.sep + "log"
# print("log : " + _log_path)
_report_path = project_path + os.sep + "report"
# print("report : "+ _report_path)
# 数据库配置信息
DB_CONFIG= {
    "host": "192.168.232.128",
    "user": "root",
    "password": "123456",
    "charset": "utf8",
    "database": "test",
    "port": 33506
}


# 返回log目录
def get_log_path():
    return _log_path


# 返回report目录
def get_report_path():
    return _report_path


# 返回config目录
def get_config_path():
    return _config_path


# 占位用，误删除，不太理解hhh
class DynamicParam:
    pass


if __name__ == '__main__':
    print(get_log_path())
