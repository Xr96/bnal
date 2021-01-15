# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 14:10
# @Author  : Fighter.Wu
import logging

fm = "%(asctime)s-%(levelname)s-[%(filename)s-%(funcName)s()-%(lineno)d行]-%(message)s"
logging.basicConfig(level=logging.INFO,format=fm,filename="./hello.log")

def log1():
    logging.info(">信息级别info")
    logging.warning(">warning")
    logging.error(">error")
    logging.critical(">critical")

log1()