# -*- coding: utf-8 -*-
import re

import requests

from exts import db
from models import UserModel


def Bind_cookie(message, qq, gid):
    '''
    绑定ck
    :param message:
    :param qq:
    :param gid:
    :return:
    '''
    try:
        cookie = re.findall('&#91;(.*?)&#93;', message)[0]
        uid = re.findall('&#91;(.*?)&#93;', message)[1]
        uid_model = UserModel.query.filter_by(qq=qq).first()      # 查询
        if uid_model:
            # 如果uid已经存在, 则返回提示信息
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, '亲爱的旅行者，当前的账号已经绑定过ck啦\n输入 .查询ck即可查询当前QQ号绑定的ck'))
        else:
            # 未存在则提交表单
            bot_user = UserModel(qq=qq, uid=uid, cookie=cookie)
            db.session.add(bot_user)
            db.session.commit()  # 提交表单
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, '绑定成功！狠狠的使用我吧~'))
    except:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, '旅行者！请再次检查输入的格式是否正确！\n格式 .绑定ck [cookie][uid]'))


def query_cookie(qq, gid):
    '''
    查询ck
    :param qq:
    :param gid:
    :return:
    '''
    qq_model = UserModel.query.filter_by(qq=qq).first()
    if qq_model:
        # 获取查询到的ck
        query_ck = qq_model.cookie
        message1 = '[CQ:at,qq={0}]\nQQ号({1})绑定的ck为：{2}'.format(qq, qq, query_ck)
        url1 = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message1)
        requests.get(url=url1)
    else:
        # 未查询到ck则反馈信息
        message2 = '[CQ:at,qq={0}]\n未查询到QQ号({1})绑定的ck'.format(qq, qq)
        url2 = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message2)
        requests.get(url=url2)


def renew_ck(qq, gid):
    '''
    替换ck
    :param qq:
    :param gid:
    :return:
    '''
    pass