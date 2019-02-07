# -*- coding: utf-8 -*-
""" entry.py
entry page

2019/2/6 y.ikeda
"""

from flask import Flask, render_template, request
from common import PAGE_TITLE

def main():
    return render_template(
        'entry.html',
        page_title=u'xxaaあxx'
    )
