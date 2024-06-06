# coding=utf-8
from config.settings import get_log_path
import logging
import time
import os

# 设置变量，目的为了控制日志信息是否在控制台输出，True为输出，False为不输出
STREAM = True


class LogUtil:
    def __init__(self):
        # 初始化日志对象 日志记录器，设置日志名称 引号内容无限制
        self.logger = logging.getLogger("logger")
        # 设置总的日志级别开关 最细 还要 INFO WARNING ERROR CRITICAL
        self.logger.setLevel(logging.DEBUG)
        # 避免日志重复 self.logger.handlers 是在 Python 的 logging 模块中使用的一个属性，它返回当前 logger 对象所有已添加的日志处理器（handlers）的列表
        # 如果self.logger没有任何处理程序（即self.logger.handlers是一个空列表），则执行随后的代码块。
        # 这通常用于在初始化日志记录器时，如果还没有添加任何处理程序，则添加默认的处理程序。例如：
        if not self.logger.handlers:
            # 带handler 的 都是处理器
            # 定义日志名称 time.strftim 把获取到到的时间转换成固定的格式
            self.log_name = '{}.log'.format(time.strftime("%Y_%m_%d", time.localtime()))
            # 定义日志路径及文件名称 拼接
            self.log_path_file = os.path.join(get_log_path(), self.log_name)
            # 定义文件处理handler 文件处理器 mode = w 先删后写
            fh = logging.FileHandler(self.log_path_file, encoding='utf-8', mode='w')
            # 设置文件处理handler的日志级别 DEBUG 是最详细的日志信息
            fh.setLevel(logging.DEBUG)
            # 日志格式变量 打印日志的时间、名称、行号、日志级别、日志信息
            formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            # 设置打印格式
            fh.setFormatter(formatter)
            # 添加handler
            # fh 为已经创建好的实例数据 需要将它添加到你的日志记录器（logger）实例中，这样日志记录器才知道应该将日志消息发送到哪些目的地。
            self.logger.addHandler(fh)
            # 关闭handler
            fh.close()
            # 控制台输出
            if STREAM:
                # 定义控制台输出流handler
                fh_stream = logging.StreamHandler()
                # 控制台输出日志级别
                fh_stream.setLevel(logging.DEBUG)
                # 设置打印格式
                fh_stream.setFormatter(formatter)
                # 添加handler
                self.logger.addHandler(fh_stream)

# 感觉上面的总结就是定义文件处理器和控制台处理器
# 文件处理器：1.创建文件记录器（即日志对象），设置其日志级别；2.创建文件处理器（地址，编码类型，操作样式）：日志级别、打印格式，将其添加至文件记录器，便于后续使用；
# 控制台处理器： 创建控制台处理器：日志类别，打印格式；将其添加至文件记录器
# 返回 定义好的looger对象，对外直接使用log函数
    def log(self):
        # 返回定义好的logger对象，对外直接使用log函数即可
        return self.logger


logger = LogUtil().log()
# 测试代码
if __name__ == '__main__':
    logger.info('test')
