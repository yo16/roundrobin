# -*- coding: utf-8 -*-
""" regist.py
regist (not page)

2019/2/17 y.ikeda
"""

from flask import Flask, render_template, request, redirect
import re

from models import regist_roundrobin

def main():
    # 引数を取得
    p_name = request.form['txt_tournament_name']
    p_detail = request.form['area_detail']
    p_ground_num = int(request.form['sel_num_of_ground'])
    p_players = re.split('[\r\n]+', request.form['area_players'])

    # 登録
    dbkey, uri = regist_roundrobin(p_name, p_detail, p_ground_num, p_players)

    # 得たURIを使ってリダイレクト
    return redirect('/r?%s' % (str(uri)))

