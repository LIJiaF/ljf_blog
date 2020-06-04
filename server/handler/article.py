from datetime import datetime
import json
import os

from tornado.web import RequestHandler
from model import DBSession, Article
from config import domain_name


class ArticleListHandler(RequestHandler):
    def get(self):
        cur_page = self.get_argument('cur_page', '1')
        page_size = 5

        sql = """
            select (
                select count(id)
                from article
            ) as total, *
            from article
            order by id desc
            limit %d offset %d
        """ % (page_size, (int(cur_page) - 1) * page_size)

        session = DBSession()
        cursor = session.execute(sql)
        data = cursor.fetchall()

        table_data = {
            'data': [],
            'page_size': page_size,
            'total': data[0]['total'] if data else 0
        }

        for d in data:
            table_data['data'].append({
                'id': d.id,
                'image_url': domain_name + d.image_url,
                'title': d.title,
                'author': d.author,
                'create_date': d.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                'write_date': d.write_date.strftime('%Y-%m-%d %H:%M:%S'),
            })

        return self.finish(json.dumps(table_data))


class ArticleHandler(RequestHandler):
    def get(self):
        article_id = self.get_argument('article_id', None)

        session = DBSession()
        article = session.query(Article).filter_by(id=article_id).first()
        if not article:
            return self.finish(json.dumps({'code': -1, 'msg': '该文章不存在'}))

        result = {
            'id': article.id,
            'image_url': (domain_name + article.image_url) if article.image_url else '',
            'title': article.title,
            'content': article.content
        }

        return self.finish(json.dumps({'code': 0, 'data': result}))

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
            return self.finish(json.dumps({'code': -1, 'msg': '添加失败'}))

        return self.finish(json.dumps({'code': 0, 'msg': '添加成功'}))

    def put(self):
        article_id = self.get_body_argument('id', None)
        title = self.get_body_argument('title', None)
        image_url = self.get_body_argument('image_url', None)
        content = self.get_body_argument('content', None)

        session = DBSession()
        article = session.query(Article).filter_by(id=article_id).first()
        if not article:
            return self.finish(json.dumps({'code': -1, 'msg': '该文章不存在'}))

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'title': title,
            'content': content,
            'write_date': now
        }

        try:
            image_url = image_url.lstrip(domain_name)
            if article.image_url and image_url != article.image_url:
                os.remove(article.image_url)
                data['image_url'] = image_url

            session.query(Article).filter_by(id=article_id).update(data)
            session.commit()
            session.close()
        except Exception as e:
            print(e)
            return self.finish(json.dumps({'code': -1, 'msg': '修改失败'}))

        return self.finish(json.dumps({'code': 0, 'msg': '修改成功'}))

    def delete(self):
        article_id = self.get_argument('article_id', None)

        session = DBSession()
        article = session.query(Article).filter_by(id=article_id).one()
        if not article:
            self.finish(json.dumps({'code': -1, 'msg': '删除失败'}))

        try:
            session.query(Article).filter_by(id=article_id).delete()
            session.commit()
        except Exception as e:
            print(e)
            return self.finish(json.dumps({'code': -1, 'msg': '删除失败'}))

        return self.finish(json.dumps({'code': 0, 'msg': '删除成功'}))
