from flask import Flask, request
from flask_migrate import Migrate

import config
from exts import db
from menu import Menu

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)    # 绑定db
migrate = Migrate(app, db)


@app.route('/', methods=['POST'])
def Get_Message():
    '''
    监听消息
    :return:
    '''
    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息 private 私聊消息
        gid = request.get_json().get('group_id')  # 获取群号
        qq = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        Menu(message, qq, gid)

    return 'OK'

if __name__ == '__main__':
    app.run()
