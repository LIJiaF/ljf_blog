from tornado.web import RequestHandler
from model import DBSession
from config import domain_name


class ShowHandler(RequestHandler):
    def get(self, article_id):
        new_sql = """
            select a.id, a.class_id, ac.name, a.title, a.author, a.note, a.content, a.write_date
            from article a
            inner join article_class ac on ac.id = a.class_id
            where a.id = %d
        """ % int(article_id)

        hot_sql = """
            select a.id, ac.name, a.image_url, a.title, a.author, a.note, a.write_date
            from article a
            inner join article_class ac on ac.id = a.class_id
            where ac.id = 1
            order by id desc
            limit 5
        """

        class_sql = """
            with cla_count as (
                select class_id, count(id) as total
                from article
                group by class_id
            )
            select ac.id, ac.name, cc.total
            from article_class as ac
            inner join cla_count as cc on cc.class_id = ac.id
            order by ac.id
        """

        session = DBSession()
        cursor = session.execute(new_sql)
        new_data = cursor.fetchall()

        cursor = session.execute(hot_sql)
        hot_data = cursor.fetchall()

        cursor = session.execute(class_sql)
        class_data = cursor.fetchall()

        new_result = {}
        for d in new_data:
            new_result = {
                'id': d.id,
                'class_id': d.class_id,
                'class_name': d.name,
                'title': d.title,
                'author': d.author,
                'note': d.note,
                'content': d.content,
                'write_date': d.write_date.strftime('%Y-%m-%d %H:%M:%S'),
            }

        hot_result = []
        for d in hot_data:
            image_url = d.image_url
            if not image_url:
                image_url = 'article/images/default.png'
            hot_result.append({
                'id': d.id,
                'class_name': d.name,
                'image_url': domain_name + image_url,
                'title': d.title,
                'author': d.author,
                'note': d.note,
                'write_date': d.write_date.strftime('%Y-%m-%d %H:%M:%S'),
            })

        class_result = []
        for d in class_data:
            class_result.append({
                'id': d.id,
                'name': d.name,
                'total': d.total
            })

        data = {
            'class_data': class_result,
            'new_data': new_result,
            'hot_data': hot_result
        }
        self.render("show.html", data=data)
