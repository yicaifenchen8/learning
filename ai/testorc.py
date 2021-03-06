# -*- coding: utf-8 -*-
from aip import AipOcr
import json
import sys

# 定义常量 
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象 
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片 
filePath = "../res/orc.jpg"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

    # 定义参数变量


options = {
    'detect_direction': 'false',
    'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(result)

print(result['words_result'])

# 解决中午转json编码问题
str = json.dumps(result, ensure_ascii=False)
print(str)



