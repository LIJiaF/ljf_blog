import json

from .base import RequestHandler, DBSession, User


class ArticleHandler(RequestHandler):
    def get(self):
        session = DBSession()
        new_user = User(name='haha')
        session.add(new_user)
        session.commit()
        session.close()

    def post(self):
        self.finish(json.dumps({'msg': 'post'}))
