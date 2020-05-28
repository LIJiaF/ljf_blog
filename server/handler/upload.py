import os
import json
import time
import random

from allow_origin import BaseHandler
from config import images_dir


class UploadHandler(BaseHandler):
    def set_default_headers(self):
        self.allowOrigin()

    def return_msg(self, msg, code=-1, **kwargs):
        state = 400
        if not code:
            state = 200
        self.set_status(state)
        result = {
            'code': code,
            'msg': msg
        }
        result.update(kwargs)
        self.finish(json.dumps(result))

    def post(self):
        file_metas = self.request.files.get('file', None)
        if not file_metas:
            return self.return_msg('文件上传失败')
        else:
            for meta in file_metas:
                try:
                    if meta['content_type'] not in ('image/jpeg', 'image/png'):
                        return self.return_msg('文件类型错误')

                    if len(meta['body']) > 2 * 1024 * 1024:
                        return self.return_msg('文件大小超过2M')

                    postfix = os.path.splitext(meta['filename'])[-1]
                    filename = str(int(time.time())) + str(random.randint(100, 999)) + postfix
                    file_path = os.path.join(images_dir, filename)

                    with open(file_path, 'wb') as up:
                        up.write(meta['body'])
                except Exception as e:
                    return self.return_msg('文件上传失败')

            return self.return_msg('文件上传成功', 0, image_url='/'.join([images_dir, filename]))
