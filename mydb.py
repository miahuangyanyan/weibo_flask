#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask_pymongo import PyMongo

from recommendlist import *


def return_img_stream(img_local_path):
    import base64
    img_stream = ''
    with open(img_local_path, 'r') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
    return img_stream


class MyMongo(object):
    def __init__(self, app):
        self.mongo = PyMongo(app)

    def get_creator_collection(self):
        return self.mongo.db.cast_personas

    def get_image_collection(self):
        return self.mongo.db.creator_img

    def get_movie_box_office(self):
        return self.mongo.db.YPEMovie

    def get_recommend(self):
        return self.mongo.db.recommend

    def get_predict(self):
        return self.mongo.db.movie_box

    def GetCreatorData(self, username):
        appusage_data = self.get_creator_collection().find_one_or_404({'name': username})
        print(appusage_data['occupation'])
        print('演员' in appusage_data['occupation'])
        if '演员' in appusage_data['occupation']:
            print("hahah")
            return [
                {"job": "演员"},
                {"name": appusage_data['figure'], "value": appusage_data['figure']},
                {"name": appusage_data['actor_overall'], "value": appusage_data['actor_overall']},
                {"name": appusage_data['voice'], "value": appusage_data['voice']},
                {"name": appusage_data['line_ability'], "value": appusage_data['line_ability']},
                {"name": appusage_data['acting'], "value": appusage_data['acting']},
                {"name": appusage_data['appearance'], "value": appusage_data['appearance']},
                # {"name" : appusage_data['temperament'], "value": appusage_data['temperament']},
                {"name": appusage_data['num_fan'], "value": appusage_data['num_fan'] / 10000000.0}
            ]
        elif '导演' in appusage_data['occupation']:
            return [
                {"job": "导演"},
                {"name": appusage_data['movie_pace'], "value": appusage_data['movie_pace']},
                {"name": appusage_data['director_overall'], "value": appusage_data['director_overall']},
                {"name": appusage_data['character'], "value": appusage_data['character']},
                {"name": appusage_data['num_fan'], "value": appusage_data['num_fan']},
            ]
        return []

    def GetMovieBoxOffice(self, username):
        movie_box_office = []
        movie_name_list = []
        ret = self.get_movie_box_office().find({'actor': {'$regex': username}})
        for x in ret:
            movie_box_office.append(int(x['total_boxoffice']))
            movie_name_list.append(x['movie_name'])
        return movie_box_office, movie_name_list

    def GetRecommendData(self, form):
        gen_list = RecommendList()
        print({
            'isSequel': (form.is_sequel.data),
            'is_GoldType': (form.is_gold_type.data),
            'Publisher': form.publisher.data,
            'movie_budget': int(form.movie_budget.data),
            'movie_type': form.movie_type.data})
        ret = self.get_recommend().find_one_or_404({
            'isSequel': (form.is_sequel.data),
            'is_GoldType': (form.is_gold_type.data),
            'Publisher': form.publisher.data,
            'movie_budget': int(form.movie_budget.data),
            'movie_type': form.movie_type.data})

        if ret != None:
            gen_list.mylist[0].name = ret['Director']
            gen_list.mylist[0].job = '导演'
            gen_list.mylist[1].name = ret['actor1']
            gen_list.mylist[1].job = '演员1'
            gen_list.mylist[2].name = ret['actor2']
            gen_list.mylist[2].job = '演员2'
            gen_list.mylist[3].name = ret['actor3']
            gen_list.mylist[3].job = '演员3'
            gen_list.mylist[4].name = ret['actor4']
            gen_list.mylist[4].job = '演员4'
            print(gen_list.mylist[0].name)
            print(self.GetCreatorPhoto(gen_list.mylist[0].name))
            for i in range(5):
                gen_list.mylist[i].photo = self.GetCreatorPhoto(gen_list.mylist[i].name)
            print(gen_list.mylist)
        return gen_list

    def GetCreatorPhoto(self, username):
        ret = self.get_image_collection().find_one_or_404({'creator_name': username})
        print(ret)
        return ret['img']

    def GetPredictData(self, form):
        print({
            "Publisher": form.publisher.data,
            "isSequel": str(form.is_sequel.data),
            "is_GoldType": str(form.is_gold_type.data),
            "movie_budget": int(form.movie_budget.data),
            "Director": form.director.data,
            "actor1": form.actor1.data,
            "actor2": form.actor2.data,
            "actor3": form.actor3.data,
            "actor4": form.actor4.data,
            "movie_type": form.movie_type.data
        }
        )
        ret = self.get_predict().find_one_or_404({
            "Publisher": form.publisher.data,
            "isSequel": str(form.is_sequel.data),
            "is_GoldType": str(form.is_gold_type.data),
            "movie_budget": int(form.movie_budget.data),
            "Director": form.director.data,
            "actor1": form.actor1.data,
            "actor2": form.actor2.data,
            "actor3": form.actor3.data,
            "actor4": form.actor4.data,
            "movie_type": form.movie_type.data
        })
        print(ret['Publisher'])
        print(form.actor1.data)
        print(form.actor2.data)
        print(form.actor3.data)
        print(form.actor4.data)
        print(form.is_gold_type.data)
        print(form.is_sequel.data)
        print(form.movie_budget.data)

        print (ret['box_office'])
        return ret
