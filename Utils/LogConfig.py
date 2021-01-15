# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 16:14
# @Author  : Fighter.Wu
import logging.handlers
import os

def Logg():
    # 声明文件
    logger = logging.getLogger()

    # 设置全局日志级别
    logger.setLevel(logging.DEBUG)

    # 声明控制器
    sh = logging.StreamHandler()
    # 日志级别
    sh.setLevel(logging.INFO)

    # 日志存放位置
    logPath = "./Log" + os.sep + "bnal.log"
    # 文件处理器
    trfh = logging.handlers.TimedRotatingFileHandler(logPath, when="midnight", interval=1, backupCount=7, encoding="utf-8")

    # 日志添加器 文件
    logger.addHandler(trfh)
    # 日志添加器 控制器
    logger.addHandler(sh)

    # 格式化
    fm = "%(asctime)s-%(levelname)s-[%(filename)s-%(funcName)s()-%(lineno)d行]-%(message)s"
    # 设置控制器处理器
    formatter = logging.Formatter(fm)
    trfh.setFormatter(formatter)
    sh.setFormatter(formatter)