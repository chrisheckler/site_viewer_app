# Copyright (2018) Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, flash, render_template, Markup, redirect
import webbrowser
import random
import sys
import click
import os
import keyboard

app = Flask(__name__)
app.secret_key = os.urandom(24)

# List of interesting sites to randomly view
site_list = ['http://fastml.com/', 'http://andrewgelman.com/',
             'http://www.walkingrandomly.com/', 'https://www.kdnuggets.com/',
             'http://blog.kaggle.com/', 'http://www.dataminingblog.com/',
             'https://miningthesocialweb.com/', 'https://hilarymason.com/',
             'http://www.becomingadatascientist.com/',
             'http://flowingdata.com/']


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
