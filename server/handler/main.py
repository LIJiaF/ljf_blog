from tornado.web import RequestHandler
from model import DBSession
from config import domain_name


class MainHandler(RequestHandler):
    def get(self):
        cur_page = self.get_argument('page', '1')
        page_size = 10

        new_sql = """
            select a.id, ac.name, a.image_url, a.title, a.author, a.note, a.create_date, a.write_date
            from article a
            inner join article_class ac on ac.id = a.class_id
            order by id desc
            limit %d offset %d
        """ % (page_size, (int(cur_page) - 1) * page_size)

        hot_sql = """
            select a.id, ac.name, a.image_url, a.title, a.author, a.note, a.create_date, a.write_date
            from article a
            inner join article_class ac on ac.id = a.class_id
            where ac.id = 1
            order by id desc
            limit 5
        """

        class_sql = """
            select ac.id, ac.name
            from article_class as ac
            where ac.id in (select distinct class_id from article)
            order by ac.id
        """

        session = DBSession()
        cursor = session.execute(new_sql)
        new_data = cursor.fetchall()

        cursor = session.execute(hot_sql)
        hot_data = cursor.fetchall()

        cursor = session.execute(class_sql)
        class_data = cursor.fetchall()

        new_result = []
        for d in new_data:
            image_url = d.image_url
            if not image_url:
                image_url = 'article/images/default.png'
            new_result.append({
                'id': d.id,
                'class_name': d.name,
                'image_url': domain_name + image_url,
                'title': d.title,
                'author': d.author,
                'note': d.note,
                'create_date': d.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                'write_date': d.write_date.strftime('%Y-%m-%d %H:%M:%S'),
            })

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
                'create_date': d.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                'write_date': d.write_date.strftime('%Y-%m-%d %H:%M:%S'),
            })

        class_result = []
        for d in class_data:
            class_result.append({
                'id': d.id,
                'name': d.name
            })

        next_page = int(cur_page) + 1
        data = {
            'class_data': class_result,
            'new_data': new_result,
            'hot_data': hot_result,
            'next_page': next_page
        }
        self.render("index.html", data=data)
