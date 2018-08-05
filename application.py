# Copyright (2018) Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask
import webbrowser
import random


app = Flask(__name__)

# List of interesting sites to randomly view
site_list = ['http://fastml.com/', 'http://andrewgelman.com/',
             'http://www.walkingrandomly.com/', 'https://www.kdnuggets.com/',
             'http://blog.kaggle.com/', 'http://www.dataminingblog.com/',
             'https://miningthesocialweb.com/', 'https://hilarymason.com/',
             'http://www.becomingadatascientist.com/',
             'http://flowingdata.com/']


@app.route('/')
def site_viewer():
    return webbrowser.open(random.choice(site_list))

if __name__ == '__main__':
    app.run()
