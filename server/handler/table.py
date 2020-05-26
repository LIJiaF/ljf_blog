from .base import RequestHandler, create_table, drop_table


class CreateTableHandler(RequestHandler):
    def get(self):
        create_table()


class DropTableHandler(RequestHandler):
    def get(self):
        drop_table()
