import tornado.web
from tornado.escape import json_decode
import pymysql
from pprint import pprint
from app.login.action import LoginPostHandler
import json
from app.main.view import BaseHandler



class LoginHandler(BaseHandler):

    def initialize(self):
        """
        当使用原生sql
        :return:
        """
        # self.conn, self.cursor = None, None
        # try:
        #     self.conn = pymysql.connect(host='127.0.0.1', password='123456', database='hotme', user='root', port=3306)
        #     self.cursor = self.conn.cursor()
        # except Exception as e:
        #     pprint("连接数据库异常: %s" % e)
        # else:
        #     pprint("连接数据库成功")
        # pprint("<initialize>方法")
        pass

    def prepare(self):
        # 这里获取一下请求的信息
        request_info = self.request.headers
        print("请求信息: %s" % request_info)
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    def get(self, *args, **kwargs):
        ret_dict = {'ret': 0}
        if not self.current_user:
            ret_dict["ret"] = 1
        else:
            ret_dict["user"] = self.current_user
        self.write(json.dumps(ret_dict))

    def post(self, *args, **kwargs):
        login_post_handler = LoginPostHandler(self)
        op_handle = login_post_handler.get_handler()
        ret_dict = op_handle()
        self.write(json.dumps(ret_dict))

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def on_finish(self):
        print(self.get_secure_cookie("user"))
        # if self.conn:
        #     self.conn.close()