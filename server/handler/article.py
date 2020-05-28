from datetime import datetime
import json

from tornado.web import RequestHandler
from model import DBSession, Article


class ArticleHandler(RequestHandler):
    def get(self):
        pass

    def post(self):
        title = self.get_body_argument('title', None)
        image_url = self.get_body_argument('image_url', None)
        content = self.get_body_argument('content', None)

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'title': title,
            'image_url': image_url,
            'content': content,
            'author': 'LiJiaF',
            'create_date': now,
            'write_date': now
        }

        try:
            session = DBSession()
            new_article = Article(**data)
            session.add(new_article)
            session.commit()
            session.close()
        except Exception as e:
            print(e)
            self.finish(json.dumps({'code': -1, 'msg': '添加失败'}))

        self.finish(json.dumps({'code': 0, 'msg': '添加成功'}))
