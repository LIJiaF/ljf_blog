import os
import json
import time
import random

from allow_origin import BaseHandler
from config import images_dir


class UploadHandler(BaseHandler):
    def set_default_headers(self):
        self.allowOrigin()

    def post(self):
        result = {'code': 0, 'msg': '上传成功'}

        file_metas = self.request.files.get('file', None)
        if not file_metas:
            result['code'] = -1
            result['msg'] = '上传文件为空'
            self.set_status(400)
            self.finish(json.dumps(result))
        else:
            for meta in file_metas:
                try:
                    postfix = os.path.splitext(meta['filename'])[-1]
                    filename = str(int(time.time())) + str(random.randint(100, 999)) + postfix
                    file_path = os.path.join(images_dir, filename)

                    with open(file_path, 'wb') as up:
                        up.write(meta['body'])
                except Exception as e:
                    result['code'] = -1
                    result['msg'] = '上传文件失败'
                    self.set_status(400)
                    self.finish(json.dumps(result))

            result['image_url'] = '/'.join([images_dir, filename])

        self.finish(json.dumps(result))
