# -*- coding: utf-8 -*-
import requests


def Color_map(message, gid):
    '''
    0为非 R18，1为 R18，2为混合
    :param message:
    :param gid:
    :return:
    '''
    url = 'https://api.lolicon.app/setu/v2'
    if message[3:5] in ['R', ' R']:
        params = {
            'r18': '1',
            'size': 'regular'
        }
        response = requests.get(url=url, params=params).json()
        pic_url = response['data'][0]['urls']['regular']
        # requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,file=' + str(pic_url) + r']'))
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, '有内鬼终止交易!'))
        print(1)
    else:
        params = {
            'size': 'regular'
        }
        response = requests.get(url=url, params=params).json()
        pic_url = response['data'][0]['urls']['regular']
        # requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,file=' + str(pic_url) + r']'))
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, '有内鬼终止交易!'))
        print(2)
