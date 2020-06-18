from tornado.web import RequestHandler
from model import DBSession
from config import domain_name


class ListHandler(RequestHandler):
    def get(self, class_id):
        cur_page = self.get_argument('page', '1')
        page_size = 10

        class_id = int(class_id) if class_id else -1

        new_sql = """
            select a.id, a.class_id, ac.name, a.image_url, a.title, a.author, a.note, a.write_date
            from article a
            inner join article_class ac on ac.id = a.class_id
            where ac.id = %d
            order by id desc
            limit %d offset %d
        """ % (class_id, page_size, (int(cur_page) - 1) * page_size)

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

        new_result = []
        for d in new_data:
            image_url = d.image_url
            if not image_url:
                image_url = 'article/images/default.png'
            new_result.append({
                'id': d.id,
                'class_id': d.class_id,
                'class_name': d.name,
                'image_url': domain_name + image_url,
                'title': d.title,
                'author': d.author,
                'note': d.note,
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
                'write_date': d.write_date.strftime('%Y-%m-%d %H:%M:%S'),
            })

        class_result = []
        for d in class_data:
            class_result.append({
                'id': d.id,
                'name': d.name,
                'total': d.total
            })

        next_page = int(cur_page) + 1
        data = {
            'class_data': class_result,
            'new_data': new_result,
            'hot_data': hot_result,
            'next_page': next_page,
            'cur_class': class_id
        }
        self.render("list.html", data=data)
