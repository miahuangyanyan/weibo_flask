#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from wtforms.fields import (StringField, PasswordField, DateField, BooleanField,
                            SelectField, SelectMultipleField, TextAreaField,
                            RadioField, IntegerField, DecimalField, SubmitField)
from flask_wtf import Form


class myform(Form):
    movie_type_option = [("动作", "动作"), ("爱情", "爱情"), ("奇幻", "奇幻"), ("剧情", "剧情"),("惊悚", "惊悚"),("冒险", "冒险"),
                         ("犯罪", "犯罪")]
    movie_publisher_option = [('a万达影视传媒有限公司 Wanda Media Co., Ltd', '万达影视传媒有限公司 Wanda Media Co., Ltd'), ('亚太未来影视（北京）有限公司 Yatai Weilai Entertainment（Beijing）Co.,Ltd', '亚太未来影视（北京）有限公司 Yatai Weilai Entertainment（Beijing）Co.,Ltd'), ("欢乐电影(上海)有限公司", "欢乐电影(上海)有限公司"),
                              ("\'中国电影股份有限公司\'", "中国电影股份有限公司"),]
    movie_budget = StringField('电影预算')
    movie_type = SelectField('电影类型', choices=movie_type_option)
    is_gold_type = SelectField('是否黄金档', choices=[("YES", 'YES'), ("NO", 'NO')])
    is_sequel = SelectField('是否续集', choices=[("YES", 'YES'), ("NO", 'NO')])
    publisher = SelectField('发行公司', choices=movie_publisher_option)
    director = StringField('导演')
    actor1 = StringField('演员1')
    actor2 = StringField('演员2')
    actor3 = StringField('演员3')
    actor4 = StringField('演员4')
    submit = SubmitField('提交')


class NameForm(Form):
    username = StringField('名字')
    submit = SubmitField('搜索')
