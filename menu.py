# -*- coding: utf-8 -*-
from blueprints import Color_Map, Cookie, Renew_role, Get_role


def Menu(message, qq, gid=None):
    '''
    功能组件
    :param message:
    :param uid:
    :param gid:
    :return:
    '''
    # 判断用户输入的功能
    if message[0] == '#':
        if message[1:3] == 'st':
            # 色图
            Color_Map.Color_map(message, gid)
        if message[1:5] == '绑定ck':
            # 绑定ck
            Cookie.Bind_cookie(message, qq, gid)
        if message[1:5] == '查询ck':
            # 查询ck
            Cookie.query_cookie(qq, gid)
        if message[1:7] == '更新角色攻略':
            # 更新角色攻略
            Renew_role.renew_role(gid)
    if message[0:4] == 'role':
        # 查询角色攻略
        Get_role.get_role(message, gid)






