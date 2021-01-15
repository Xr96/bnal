# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 15:16
# @Author  : Fighter.Wu
import logging.handlers

# 声明日志器
import os

logger = logging.getLogger()
# 设置级别
logger.setLevel(logging.INFO)

logPath = "../Log" + os.sep + "hm.log"

# 设置控制器
trfh = logging.handlers.TimedRotatingFileHandler(logPath,when="midnight",interval=1,backupCount=7,encoding="utf-8")

logger.addHandler(trfh)

fmr = "%(asctime)s-%(levelname)s-[%(filename)s-%(funcName)s()-%(lineno)d行]-%(message)s"

formatter = logging.Formatter(fmr)

trfh.setFormatter(formatter)


logging.info("info")
logging.warning("warning")
logging.error("error")
