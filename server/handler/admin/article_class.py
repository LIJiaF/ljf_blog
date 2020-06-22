from datetime import datetime
import json

from tornado.web import RequestHandler
from model import DBSession, ArticleClass
from common import log


class ArticleClassAllHandler(RequestHandler):
    def get(self):
        session = DBSession()
        data = session.query(ArticleClass).all()

        result = []
        for d in data:
            result.append({
                'id': d.id,
                'name': d.name
            })

        return self.finish(json.dumps(result))


class ArticleClassListHandler(RequestHandler):
    def get(self):
        cur_page = self.get_argument('cur_page', '1')
        page_size = 5

        log.info('获取文章分类列表cur_page：' + cur_page)

        sql = """
            select (
                select count(id)
                from article_class
            ) as total, *
            from article_class
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
                'name': d.name,
                'create_date': d.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                'write_date': d.write_date.strftime('%Y-%m-%d %H:%M:%S'),
            })

        return self.finish(json.dumps(table_data))


class ArticleClassHandler(RequestHandler):
    def get(self):
        class_id = self.get_argument('class_id', None)

        log.info('获取文章分类信息：class_id ' + class_id)

        session = DBSession()
        article_class = session.query(ArticleClass).filter_by(id=class_id).first()
        if not article_class:
            return self.finish(json.dumps({'code': -1, 'msg': '该分类不存在'}))

        result = {
            'id': article_class.id,
            'name': article_class.name
        }

        return self.finish(json.dumps({'code': 0, 'data': result}))

    def post(self):
        name = self.get_body_argument('name', None)

        log.info('添加文章分类：' + name)

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'name': name,
            'create_date': now,
            'write_date': now
        }

        try:
            session = DBSession()
            new_class = ArticleClass(**data)
            session.add(new_class)
            session.commit()
            session.close()
        except Exception as e:
            print(e)
            return self.finish(json.dumps({'code': -1, 'msg': '添加失败'}))

        return self.finish(json.dumps({'code': 0, 'msg': '添加成功'}))

    def put(self):
        class_id = self.get_body_argument('class_id', None)
        name = self.get_body_argument('name', None)

        log.info('修改文章分类：class_id ' + class_id + ' => ' + name)

        session = DBSession()
        article_class = session.query(ArticleClass).filter_by(id=class_id).first()
        if not article_class:
            return self.finish(json.dumps({'code': -1, 'msg': '该分类不存在'}))

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'name': name,
            'write_date': now
        }

        try:
            session.query(ArticleClass).filter_by(id=class_id).update(data)
            session.commit()
            session.close()
        except Exception as e:
            print(e)
            return self.finish(json.dumps({'code': -1, 'msg': '修改失败'}))

        return self.finish(json.dumps({'code': 0, 'msg': '修改成功'}))

    def delete(self):
        class_id = self.get_argument('class_id', None)

        log.info('删除文章分类：class_id ' + class_id)

        session = DBSession()
        article_class = session.query(ArticleClass).filter_by(id=class_id).first()
        if not article_class:
            return self.finish(json.dumps({'code': -1, 'msg': '删除失败'}))

        try:
            session.query(ArticleClass).filter_by(id=class_id).delete()
            session.commit()
        except Exception as e:
            print(e)
            return self.finish(json.dumps({'code': -1, 'msg': '删除失败'}))

        return self.finish(json.dumps({'code': 0, 'msg': '删除成功'}))
