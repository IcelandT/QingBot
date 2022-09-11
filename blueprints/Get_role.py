# -*- coding: utf-8 -*-
import base64
import re

import requests

from models import RoleModel


def get_role(message, gid):
    role_name = re.findall('role(.*)', message)
    if role_name:
        # 角色名称
        role_name = role_name[0]
        role_model = RoleModel.query.filter_by(rolename=role_name).first()  # 查询角色信息
        if role_model:
            # 图片链接
            role_pic = role_model.rolepic_url
            # 解密
            role_pic = base64.b64decode(role_pic.encode('utf-8')).decode('utf-8')
            # 反馈信息
            message1 = '[CQ:image,file={0}]'.format(role_pic)
            url1 = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message1)
            requests.get(url=url1)
        else:
            message2 = '未查询到该角色的信息，检查一下角色名称是否正确'
            url2 = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message2)
            requests.get(url=url2)
    else:
        message2 = '未查询到该角色的信息，检查一下就角色名称是否正确'
        url2 = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message2)
        requests.get(url=url2)