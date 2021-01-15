# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 14:30
# @Author  : Fighter.Wu
import logging

# 声明日志器对象
logger = logging.getLogger()

# 设置日志级别
logger.setLevel(logging.INFO)

# 声明控制台处理器
sh = logging.StreamHandler()

# 设置控制台处理器日志最低级别  覆盖日志器日志级别
sh.setLevel(logging.ERROR)

logger.addHandler(sh)

# 日志器方法 输出日志  -不推荐使用
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

