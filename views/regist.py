# -*- coding: utf-8 -*-
""" regist.py
registed page

2019/2/17 y.ikeda
"""

from flask import Flask, render_template, request
import re

def main():
    # 引数を取得
    p_name = request.form['txt_tournament_name']
    p_detail = request.form['area_detail']
    p_ground_num = request.form['sel_num_of_ground']
    p_players = re.split('[\r\n]+', request.form['area_players'])

    return render_template(
        'roundrobin.html',
        name = p_name,
        detail = p_detail,
        ground_num = p_ground_num,
        players = p_players
    )
