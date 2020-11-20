import json
import tornado.web
import pymysql
from app.main.action import IndexPostHandler

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class ConnectMysql(tornado.web.RequestHandler):
    """
    基类
    """
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
        else:
            pass

class CreateTableHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        Base.metadata.create_all()
        self.write("创建映射表成功")

class DeleteTableHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        Base.metadata.drop_all()
        self.write("删除映射表成功")

class IndexHandler(BaseHandler):

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
        else:
            pass

    def prepare(self):
        pass

    def get(self, *args, **kwargs):
        print("登录首页")
        if not self.current_user:
            self.redirect("/login/")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render('base.html', user=name)

    def post(self, *args, **kwargs):
        index_post_handler = IndexPostHandler(self)
        op_handle = index_post_handler.get_handler()
        ret_dict = op_handle()
        self.write(json.dumps(ret_dict))

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def on_finish(self):
        if self.conn:
            self.conn.close()



class ForgetPasswordHandler(tornado.web.RequestHandler):

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
        else:
            pass

    def prepare(self):
        pass

    def get(self, *args, **kwargs):
        self.render('forget_password.html')

    def post(self, *args, **kwargs):
        self.write('忘记密码请求')

    def on_finish(self):
        if self.conn:
            self.conn.close()