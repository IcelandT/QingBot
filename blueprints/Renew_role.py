# -*- coding: utf-8 -*-
'''
更新角色攻略信息，只有拥有权限的管理员才可使用，后期添加管理员身份验证
'''
import base64
import json

import jsonpath
import requests

from exts import db
from models import RoleModel

url = 'https://bbs-api.mihoyo.com/post/wapi/getPostFullInCollection?collection_id=813033&gids=2&order_type=1'
def renew_role(gid):
    '''
    更新角色攻略
    :param message: 消息内容
    :param gid: 群号
    :return:
    '''
    response = requests.get(url=url).text
    json_data = json.loads(response)
    # 角色名称列表
    role_list = jsonpath.jsonpath(json_data, '$..subject')
    role_list = [i.split('——')[1] for i in role_list]
    # 角色攻略信息
    role_img = jsonpath.jsonpath(json_data, '$..image_list.[0].url')
    # 如果有数据返回
    if role_list:
        # 反馈信息
        message1 = '共{}个角色信息，可能会花费一段时间......'.format(len(role_list))
        url1 = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message1)
        requests.get(url=url1)
        for i in zip(role_list, role_img):
            # 加密
            rolepic_url_encode = base64.b64encode(i[1].encode('utf-8')).decode('utf-8')
            role_model = RoleModel.query.filter_by(rolename=i[0]).first()
            # 如果角色已经存在，则进行更新操作
            if role_model:
                # 更新角色url
                role_model.rolepic_url = rolepic_url_encode
                db.session.commit()
            # 如果角色不存在，则直接填入数据库当中
            else:
                role_model = RoleModel(rolename=i[0], rolepic_url=rolepic_url_encode)
                db.session.add(role_model)
                db.session.commit()
        # 反馈信息
        message2 = '更新成功!'
        url2 = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message2)
        requests.get(url=url2)
    # 如果无数据返回
    else:
        # 反馈信息
        message3 = '无数据返回，请检查接口是否能够使用'
        url3 = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message3)
        requests.get(url=url3)