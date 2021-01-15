# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 11:41
# @Author  : Fighter.Wu
import logging

fm = "%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-%(lineno)s-%(message)s"
logging.basicConfig(level=logging.INFO,format=fm)

def log1():
    logging.info(">info")
    logging.warning(">warning")
    logging.error(">error")
    logging.critical(">critical")

log1()