#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
version: python2.7      software: PyCharm
file: echart.py        time: 2017/3/5 19:56
"""
import sqlite3

from flask import Flask, render_template

from mydb import *
from myform import *
from recommendlist import *

app = Flask(__name__)
app.config.update(
    MONGO_HOST='192.168.200.47',
    # MONGO_HOST='127.0.0.1',
    MONGO_PORT=27017,
    MONGO_DBNAME='Land_Movie'
)
mymongo = MyMongo(app)


# def get_db():
#     db = sqlite3.connect(r'E:\Gitwork\echart\mydb.db')
#     db.row_factory = sqlite3.Row
#     return db
#
#
# def query_db(query, args=(), one=False):
#     db = get_db()
#     cur = db.execute(query, args)
#     # cur = db.execute("SELECT * FROM cpu WHERE id>=1")
#     db.commit()
#     rv = cur.fetchall()
#     db.close()
#     return (rv[0] if rv else None) if one else rv


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/introduce", methods=["GET"])
def introduce():
    return render_template("introduce.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = myform(csrf_enabled=False)
    if form.validate_on_submit():
        res = mymongo.GetPredictData(form)
        print ("my_res:")
        print (res)
        return render_template("predict.html", form=form, appusage_data=res)
    return render_template("predict.html", form=form)


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    form = myform(csrf_enabled=False)
    res = RecommendList()
    if form.validate_on_submit():
        res = mymongo.GetRecommendData(form)
        return render_template("recommend.html", form=form, recommend_list=res)
    return render_template("recommend.html", form=form)


@app.route("/creator/<username>")
def creator_with_username(username):
    res = mymongo.GetCreatorData(username)
    my_img_stream = mymongo.GetCreatorPhoto(username)
    my_movie_box_office, my_movie_name_list = mymongo.GetMovieBoxOffice(username)
    return render_template("creator.html", appusage_data=res, img_stream=my_img_stream,
                           movie_box_office=my_movie_box_office, movie_name_list=my_movie_name_list)


@app.route("/creator", methods=['GET', 'POST'])
def creator():
    res = None
    my_img_stream = None
    my_movie_box_office = None
    my_movie_name_list = None
    form = NameForm(csrf_enabled=False)
    if form.validate_on_submit():
        if form.username:
            username = form.username.data
            res = mymongo.GetCreatorData(username)
            my_img_stream = mymongo.GetCreatorPhoto(username)
            my_movie_box_office, my_movie_name_list = mymongo.GetMovieBoxOffice(username)
            print (my_movie_box_office)
            print (my_movie_name_list)
            return render_template("creator.html", form=form, appusage_data=res, img_stream=my_img_stream,
                                   movie_box_office=my_movie_box_office, movie_name_list=my_movie_name_list)
        else:
            return render_template("creator.html", form=form)
    return render_template("creator.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
    app.config['SECRET_KEY'] = '123456'
