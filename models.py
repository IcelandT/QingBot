# -*- coding: utf-8 -*-
from datetime import datetime

from exts import db


class UserModel(db.Model):
    ''' 用户信息模型 '''
    __tablename__ = 'bot_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)        # 设为主键，自增长
    qq = db.Column(db.String(20), nullable=False, unique=True)     # 用户QQ
    uid = db.Column(db.String(20), nullable=False, unique=True)  # 原神uid
    cookie = db.Column(db.String(300), nullable=False, unique=True)     # 账号ck
    join_time = db.Column(db.DateTime, default=datetime.now())      # 加入时间


class RoleModel(db.Model):
    ''' 角色信息模型 '''
    __tablename__ = 'roledata'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 设为主键，自增长
    rolename = db.Column(db.String(10), nullable=False, unique=True)    # 角色名称
    rolepic_url = db.Column(db.String(180), nullable=False, unique=True)    # 图片链接
