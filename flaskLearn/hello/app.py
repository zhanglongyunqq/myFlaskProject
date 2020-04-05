# -*- coding:utf-8 -*-
from flask import Flask
# from Config import Config
app = Flask(__name__)   #实例化

#the minimal Flask application
@app.route('/')                    #非变量路由参数
def index():
    return "<h1>hello,world!<h1>"

@app.route('/he/<name>')             #具有传入参数的路由name
def gret(name):
    return '<h1>hello  %s !</h1>'%name



if __name__ == "__main__":
    app.run()