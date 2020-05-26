from allow_origin import BaseHandler


class UploadHandler(BaseHandler):
    def set_default_headers(self):
        self.allowOrigin()

    def post(self):
        pass
