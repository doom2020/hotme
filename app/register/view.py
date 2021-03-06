import json
import tornado.web
import pymysql
from tornado.escape import json_decode
from app.register.action import RegisterPostHandler
from app.main.view import BaseHandler


class RegisterHandler(BaseHandler):
    
    def initialize(self):
        """
        当使用原生sql
        :return:
        """
        self.conn, self.cursor = None, None
        try:
            self.conn = pymysql.connect(host='127.0.0.1', password='123456', database='hotme', user='root', port=3306)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
        except:
            print("连接数据库成功")

    def prepare(self):
        pass

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        register_post_handler = RegisterPostHandler(self)
        op_handle = register_post_handler.get_handler()
        ret_dict = op_handle()
        self.write(json.dumps(ret_dict))

    def on_finish(self):
        if self.conn:
            self.conn.close()