class Person(object):
    def __init__(self):
        self.name = 'yourname'
        self.job = 'director'
        self.photo = ''


class RecommendList(object):
    def __init__(self, mylist=[Person(), Person(), Person(), Person(), Person()]):
        self.mylist = mylist
