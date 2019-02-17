# -*- coding: utf-8 -*-
""" regist.py
registed page

2019/2/17 y.ikeda
"""

from flask import Flask, render_template, request

def main():
    return render_template(
        'regist.html'
    )
