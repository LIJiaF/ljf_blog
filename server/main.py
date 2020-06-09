from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler

import os

from config import images_dir
from handler import *


def make_app():
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # current_path = os.path.dirname(__file__)
    setting = {
        'debug': True,
        'template_path': '../html',
    }

    return Application([
        (r'/admin/article/class', ArticleClassHandler),
        (r'/admin/article/class/list', ArticleClassListHandler),
        (r'/admin/article/class/all', ArticleClassAllHandler),
        (r'/admin/article', ArticleHandler),
        (r'/admin/article/list', ArticleListHandler),

        (r'/article', MainHandler),

        (r'/upload', UploadHandler),
        (r'/create_table', CreateTableHandler),
        (r'/drop_table', DropTableHandler),

        (r"/article/images/(.*)", StaticFileHandler, {'path': 'images'}),
        (r"/js/(.*)", StaticFileHandler, {'path': '../html/js'}),
        (r"/css/(.*)", StaticFileHandler, {'path': '../html/css'}),
        (r"/fonts/(.*)", StaticFileHandler, {'path': '../html/fonts'}),
        (r"/images/(.*)", StaticFileHandler, {'path': '../html/images'}),
    ], **setting)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
