from tornado.ioloop import IOLoop
from tornado.web import Application

from handler import *


def make_app():
    return Application([
        (r'/*', ArticleHandler),
        (r'/upload', UploadHandler),
        (r'/article', ArticleHandler),
        (r'/create_table', CreateTableHandler),
        (r'/drop_table', DropTableHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
