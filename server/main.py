from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler

import os

from config import images_dir
from handler import *


def make_app():
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    current_path = os.path.dirname(__file__)
    setting = {
        'debug': True,
        # 'static_path': os.path.join(current_path, "images"),
    }

    return Application([
        (r'/admin/article/class', ArticleClassHandler),
        (r'/admin/article/class/list', ArticleClassListHandler),
        (r'/admin/article', ArticleHandler),
        (r'/admin/article/list', ArticleListHandler),
        (r'/upload', UploadHandler),
        (r'/create_table', CreateTableHandler),
        (r'/drop_table', DropTableHandler),
        (r'/*', ArticleHandler),
        (r"/images/(.*)", StaticFileHandler, {"path": os.path.join(current_path, "images")})  # 访问静态资源路由
    ], **setting)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
