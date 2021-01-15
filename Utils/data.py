# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 10:28
# @Author  : Fighter.Wu
import json,os

class Date:

    @classmethod
    def get_json_data(cls,file):
        with open("./data"+os.sep+file,"r",encoding="utf-8") as f:
            return json.load(f)