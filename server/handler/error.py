from tornado.web import RequestHandler
from model import DBSession


class ErrorHandler(RequestHandler):
    def get(self):
        class_sql = """
            select ac.id, ac.name
            from article_class as ac
            where ac.id in (select distinct class_id from article)
            order by ac.id
        """

        session = DBSession()

        cursor = session.execute(class_sql)
        class_data = cursor.fetchall()

        session.close()

        class_result = []
        for d in class_data:
            class_result.append({
                'id': d.id,
                'name': d.name
            })

        self.render("404.html", data=class_result)
