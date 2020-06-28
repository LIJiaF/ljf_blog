from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler

import os

from common import log
from config import images_dir
from handler import *


def make_app():
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # current_path = os.path.dirname(__file__)
    setting = {
        'debug': True,
        'template_path': '../html',
        'static_path': '../html'
    }

    return Application([
        (r'/admin/article/class', ArticleClassHandler),
        (r'/admin/article/class/list', ArticleClassListHandler),
        (r'/admin/article/class/all', ArticleClassAllHandler),
        (r'/admin/article', ArticleHandler),
        (r'/admin/article/list', ArticleListHandler),

        (r'/', MainHandler),
        (r'/list/?(?P<class_id>\d*)', ListHandler),
        (r'/show/?(?P<article_id>\d*)', ShowHandler),

        (r'/upload', UploadHandler),
        (r'/create_table', CreateTableHandler),
        (r'/drop_table', DropTableHandler),

        (r"/images/article/(.*)", StaticFileHandler, {'path': 'images/article'}),
        (r"/js/(.*)", StaticFileHandler, {'path': '../html/js'}),
        (r"/css/(.*)", StaticFileHandler, {'path': '../html/css'}),
        (r"/fonts/(.*)", StaticFileHandler, {'path': '../html/fonts'}),
        (r"/images/(.*)", StaticFileHandler, {'path': '../html/images'}),
    ], **setting)


if __name__ == "__main__":
    log.info('服务器启动：127.0.0.1:8888')
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
