#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: apiAutoTest
@author: zy7y
@file: run.py
@ide: PyCharm
@time: 2020/12/16
@github: https://github.com/zy7y
@site: https://cnblogs.com/zy7y
@desc: 运行文件
"""
from string import Template
import os
import shutil
from test.conftest import pytest
from tools import logger
from tools.read_file import ReadFile
from tools.json_zhh import CJsonEncoder
from tools.send_email import EmailServe
import yaml
import jwt
import datetime
from pathlib import Path
file_path = ReadFile.read_config('$.file_path')
email = ReadFile.read_config('$.email')

# def create_token(db_wwu_id, db_wwu_name):
#     """
#     生成平台访问token
#     :author: chenWanYue
#     :param db_wwu_id:
#     :param db_wwu_name:
#     :return:
#     """
#     # 测试 #9ue0xwJQtW&i&vCSldXO5rEP9Kc&qBy
#     # 生产 1np1iWjod#HZmwUIaJOr4czT8gtCRd9o
#     payload = {
#         "id": db_wwu_id,
#         "name": db_wwu_name,
#         "type": "AccountToken",
#         "exp": int((datetime.datetime.now() + datetime.timedelta(hours=2400)).timestamp())
#     }
#     token = jwt.encode(payload=payload, key="#9ue0xwJQtW&i&vCSldXO5rEP9Kc&qBy", algorithm="HS256")
#     # token = jwt.encode(payload=payload, key="1np1iWjod#HZmwUIaJOr4czT8gtCRd9o", algorithm="HS256")
#     return token
# def yaml_template(self,data):
#     config_path = f"{str(os.path.abspath('.'))}/config/config.yaml"
#     with open(config_path, encoding="utf-8", errors='ignore') as f:
#         re = Template(f.read().encode(encoding='uft-8')).substitute(data)
#     return yaml.safe_load(re)
# def set_state(state):
#     file_name = f"{str(os.path.abspath('.'))}/config/config.yaml"
#     with open(file_name) as f:
#         doc = yaml.safe_load(f)
#     doc['state'] = state
#     with open(file_name, 'w') as f:
#         yaml.safe_dump(doc, f, default_flow_style=False)
def run():
    if os.path.exists('report/'):
        shutil.rmtree(path='report/')

    # 解决 issues 句柄无效
    logger.remove()
    logger.add(file_path['log'], enqueue=True, encoding='utf-8')
    pytest.main(
        args=[
            'test/test_api.py',
            f'--alluredir={file_path["report"]}/data'])
    logger.info(f'--alluredir={file_path["report"]}/data')
    # 自动以服务形式打开报告
    # oos.system(f'allure serve {file_path["report"]}/data')

    # 本地生成报告
    # print(file_path["report"])
    os.system(
        f'allure generate {file_path["report"]}data -o {file_path["report"]}html --clean')
    logger.success('报告已生成')

    # # 发送邮件带附件报告
    # EmailServe.send_email(email, file_path['report'])
    #
    # # 删除本地附件
    # os.remove(email['enclosures'])


if __name__ == '__main__':
    run()