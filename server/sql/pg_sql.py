import psycopg2

from config import pgsqlConfig


class PgManager(object):
    def __init__(self, config):
        self.conn = None
        self.cur = None
        self.config = config

    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.config)
            self.cur = self.conn.cursor()
        except Exception as e:
            print('数据库连接失败')
            print(e)

    def close(self):
        self.cur.close()
        self.conn.close()

    def execute(self, sql):
        count = 0
        try:
            self.connect()
            self.cur.execute(sql)
            count = self.cur.rowcount
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return count

    def fetchone(self, sql):
        self.connect()
        self.cur.execute(sql)
        columns = [col[0] for col in self.cur.description]
        row = self.cur.fetchone()
        self.close()

        return dict(zip(columns, row)) if row else row

    def fetchall(self, sql):
        self.connect()
        self.cur.execute(sql)
        columns = [col[0] for col in self.cur.description]
        rows = self.cur.fetchall()
        self.close()

        return [dict(zip(columns, row)) for row in rows] if rows else rows


if __name__ == '__main__':
    select_sql = 'select * from article'
    insert_sql = """
        insert into 
            article(title, author, content, create_date, write_date)
        values 
            ('测试测试', '李家富', '测试测试测试测试测试测试测试测试测试测试', '2020-05-20 13:14:00', '2020-05-20 13:14:00'),
            ('测试测试', '李家富', '测试测试测试测试测试测试测试测试测试测试', '2020-05-20 13:14:00', '2020-05-20 13:14:00');
    """

    pg = PgManager(pgsqlConfig)
    row = pg.execute(insert_sql)
    print(row)
