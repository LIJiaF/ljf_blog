import logging

log = logging.getLogger()
log.setLevel('DEBUG')
stream_handler = logging.StreamHandler()
fmt = logging.Formatter('输出时间:%(asctime)s -- 文件名:%(filename)s -- 行号:%(lineno)d -- 级别:%(levelname)s:%(message)s')
stream_handler.setFormatter(fmt)
stream_handler.setLevel('INFO')
log.addHandler(stream_handler)
