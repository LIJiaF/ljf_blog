from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def options(self):
        self.set_status(204)
        self.finish()

    #  允许跨域访问的地址
    def allowOrigin(self):
        allow_list = [
            'http://127.0.0.1:8080',
        ]
        if 'Origin' in self.request.headers:
            origin = self.request.headers['Origin']
            if origin in allow_list:
                self.set_header('Access-Control-Allow-Origin', origin)
                self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
