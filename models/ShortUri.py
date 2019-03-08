# -*- coding: utf-8 -*-
"""
ShortURI
"""
from google.appengine.ext import ndb
from random import randint, seed
from datetime import datetime, timedelta

# URIの文字列長
URI_STRING_LEN = 20

# 有効日数
URI_VALID_DAYS = 30


class ShortURI(ndb.Model):
    """ ShortURI
    """
    # URI
    uri = ndb.StringProperty()
    # 作成日
    create_date = ndb.DateProperty()
    # 最終アクセス日時
    last_use_datetime = ndb.DateTimeProperty()


def create_new_uri(uri_len=URI_STRING_LEN):
    """ ランダムな文字でURIを決める
    """
    use_chars = 'abcdefghijklmnopqrstuvwxyz' \
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                '1234567890'
    
    now = datetime.now()
    seed(now.hour+now.minute+now.second+now.microsecond)

    uri_is_duplicated = True
    while uri_is_duplicated:
        uri = ''
        for i in range(uri_len):
            pos = randint(0,len(use_chars)-1)
            uri += use_chars[pos]
        
        # 同じURIがなければok/あったら再作成
        u = ShortURI.query(ShortURI.uri==uri).get()
        if u is None:
            uri_is_duplicated = False
    
    return uri


def regist_uri(uri_str):
    """ 登録
    """
    uinfo = {}
    uinfo['uri'] = uri_str
    uinfo['create_date'] = datetime.today()
    uinfo['last_use_datetime'] = datetime.now()

    # 登録
    key = ShortURI(**uinfo).put()

    return key.integer_id()


def is_valid_uri(uri_str):
    """ 有効なURIかどうかを判断する
    """
    u = ShortURI.query(ShortURI.uri==uri_str).get()
    if u is None:
        return False
    
    # 最終アクセス日を取得
    last_use_dt = u.last_use_datetime
    # 期限日時
    expired_dt = last_use_dt + timedelta(days=URI_VALID_DAYS)

    # 期限日時＜今の日時　の場合はアウト
    if expired_dt < datetime.now():
        return False
    
    # 最終アクセス日時を更新しておく
    u.last_use_datetime = datetime.now()
    _ = u.put()

    return True
