from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

import json

from model import DBSession, User


class ArticleHandler(RequestHandler):
    def get(self):
        session = DBSession()
        new_user = User(name='haha')
        session.add(new_user)
        session.commit()
        session.close()

    def post(self):
        self.finish(json.dumps({'msg': 'post'}))


def make_app():
    return Application([
        (r'/*', ArticleHandler),
        (r'/article', ArticleHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
