from tornado.web import RequestHandler
from model import DBSession
from config import domain_name


class MainHandler(RequestHandler):
    def get(self):
        cur_page = self.get_argument('cur_page', '1')
        page_size = 5

        sql = """
            select a.id, ac.name, a.image_url, a.title, a.author, a.note, a.create_date, a.write_date
            from article a
            inner join article_class ac on ac.id = a.class_id
            order by id desc
            limit %d offset %d
        """ % (page_size, (int(cur_page) - 1) * page_size)

        session = DBSession()
        cursor = session.execute(sql)
        data = cursor.fetchall()

        result = []
        for d in data:
            result.append({
                'id': d.id,
                'class_name': d.name,
                'image_url': domain_name + d.image_url,
                'title': d.title,
                'author': d.author,
                'note': d.note,
                'create_date': d.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                'write_date': d.write_date.strftime('%Y-%m-%d %H:%M:%S'),
            })

        self.render("index.html", data=result)
