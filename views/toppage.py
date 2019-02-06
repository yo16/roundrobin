# -*- coding: utf-8 -*-
""" toppage.py
top page

2019/2/6 y.ikeda
"""

from flask import Flask, render_template, request

def main():
    return render_template('toppage.html')
