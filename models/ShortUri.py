# -*- coding: utf-8 -*-
"""
ShortURI
"""
from google.appengine.ext import ndb
from random import randint, seed
from datetime import datetime


class ShortURI(ndb.Model):
    """ ShortURI
    """
    # URI
    uri = ndb.StringProperty()
    # 作成日
    create_date = ndb.DateProperty()
    # 最終アクセス日時(JST)
    last_use_datetime = ndb.DateTimeProperty()


def create_new_uri(uri_len=20):
    """ ランダムな文字でURIを決める
    """
    use_chars = 'abcdefghijklmnopqrstuvwxyz' \
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                '1234567890'
    
    now = datetime.now()
    seed(now.hour+now.minute+now.second+now.microsecond)
    uri = ''
    for i in range(uri_len):
        pos = randint(0,len(use_chars)-1)
        uri += use_chars[pos]
    
    return uri

