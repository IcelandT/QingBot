'''
salt=dmq2p7ka6nsu0d3ev6nex4k1ndzrnfiy
'''
import hashlib
import random
import time


def get_timestamp():
    '''
    获取当前时间戳
    :return:
    '''
    timestamp = int(time.time())
    return timestamp

def get_randomnumbers():
    '''
    随机六位数
    :return:
    '''
    # numbers = 'abcdefghijklmnopqrstuvwxyz0123456789'
    # random_number = ''.join(random.sample(numbers, 6))
    random_number = int(random.random() * 1000000)
    return random_number

def get_DS():
    b = ''
    q = ''
    time = get_timestamp()
    random_number = get_randomnumbers()
    str = f"salt=xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs&t={time}&r={random_number}&b={b}&q={q}"
    md = hashlib.md5()
    md.update(str.encode('utf-8'))
    md5_code = md.hexdigest()
    DS = '{},{},{}'.format(time, random_number, md5_code)
    print(DS)

if __name__ == '__main__':
    get_DS()


