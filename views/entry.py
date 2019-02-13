# -*- coding: utf-8 -*-
""" entry.py
entry page

2019/2/6 y.ikeda
"""

from flask import Flask, render_template, request

def main():
    return render_template(
        'entry.html'
    )
