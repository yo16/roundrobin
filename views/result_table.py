# -*- coding: utf-8 -*-
""" result_table.py
result_table page

2019/3/6 y.ikeda
"""
from flask import Flask, render_template, request

from views import v_entry
from models import is_valid_uri, get_roundrobin

def main():
    # 引数からURIを取得
    uri_str = ''
    for arg in request.args:
        uri_str = arg
    # URIが取得できなかったらトップへ
    if len(uri_str)==0:
        return v_entry()
    
    # URIが有効なものか確認する
    if not is_valid_uri(uri_str):
        return v_entry()
    
    # RoundRobinテーブルから情報を取得する
    rr = get_roundrobin(uri_str)

    return render_template(
        'roundrobin.html',
        name = rr['name'],
        detail = rr['detail'],
        num_of_ground = rr['num_of_ground'],
        players = rr['players'],
        uri = rr['uri']
    )

