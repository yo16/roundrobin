# -*- coding: utf-8 -*-
""" result_table.py
result_table page

2019/3/6 y.ikeda
"""

from flask import Flask, render_template, request

def main():
    return render_template(
        'roundrobin.html'
    )

