from distutils.log import debug
from flask import Flask,redirect,url_for,render_template,request



app=Flask(__name__)
from app.auth import routes


if __name__ == '__main__':
    app.run()