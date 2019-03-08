# -*- coding: utf-8 -*-
"""
RoundRobin
"""
from google.appengine.ext import ndb

from .ShortUri import create_new_uri, regist_uri

class RoundRobin(ndb.Model):
    """ RoundRobin class
    """
    # 大会名
    name = ndb.StringProperty()
    # 大会名詳細
    detail = ndb.StringProperty()
    # グランド数
    num_of_ground = ndb.IntegerProperty()
    # プレイヤー
    players = ndb.StringProperty(repeated=True)
    # URI(短縮URL)
    uri = ndb.StringProperty()


def regist_roundrobin(name, detail, num_of_ground, players):
    """ RoundRobinにレコードを追加
    """
    # RoundRobin情報を作成
    rrinfo = {}
    rrinfo['name'] = name
    rrinfo['detail'] = detail
    rrinfo['num_of_ground'] = num_of_ground
    rrinfo['players'] = []
    for p in players:
        rrinfo['players'].append(p)
    uri = create_new_uri()
    rrinfo['uri'] = uri

    # 登録
    rrkey = RoundRobin(**rrinfo).put()

    # URIも登録
    _ =regist_uri(uri)

    return rrkey.integer_id(), uri


def get_roundrobin(uri_str):
    """ URIをキーにRoundRobin情報を得る
    """
    r = RoundRobin.query(RoundRobin.uri==uri_str).get()
    r_info = {
        'name': r.name,
        'detail': r.detail,
        'num_of_ground': r.num_of_ground,
        'players': [],
        'uri': uri_str
    }
    for p in r.players:
        r_info['players'].append(p)
    
    return r_info
