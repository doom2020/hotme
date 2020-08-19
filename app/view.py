import tornado.web
import pymysql
from utils.conn import Base
from app.models import *


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
        print('this is initialize')

class CreateTableHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        Base.metadata.create_all()
        self.write("创建映射表成功")

class DeleteTableHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        Base.metadata.drop_all()
        self.write("删除映射表成功")

class IndexHandler(tornado.web.RequestHandler):

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
        print('this is initialize')

    def prepare(self):
        print('this is a prepare')

    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self, *args, **kwargs):
        self.write('首页post请求')

    def patch(self, *args, **kwargs):
        self.write('首页patch请求')

    def put(self, *args, **kwargs):
        self.write('首页put请求')

    def delete(self, *args, **kwargs):
        self.write('首页delete请求')

    def on_finish(self):
        if self.conn:
            self.conn.close()
        print('on finish')

class LoginHandler(tornado.web.RequestHandler):

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
        print('this is initialize')

    def prepare(self):
        print('this is a prepare')

    def get(self, *args, **kwargs):
        # name = self.get_argument('name')
        # print(name)
        # name2 = self.get_query_argument('name')
        # print(name2)
        # self.write('登录get请求')
        return self.render('login.html')

    def post(self, *args, **kwargs):
        self.write('登录post请求')

    def on_finish(self):
        if self.conn:
            self.conn.close()
        print('on finish')

class RegisterHandler(tornado.web.RequestHandler):

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
        print('this is initialize')

    def prepare(self):
        print('this is a prepare')

    def get(self, *args, **kwargs):
        self.render('register.html')

    def post(self, *args, **kwargs):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.write('注册post请求')

    def on_finish(self):
        if self.conn:
            self.conn.close()
        print('on finish')

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
        print('this is initialize')

    def prepare(self):
        print('this is a prepare')

    def get(self, *args, **kwargs):
        self.render('forget_password.html')

    def post(self, *args, **kwargs):
        self.write('注册post请求')

    def on_finish(self):
        if self.conn:
            self.conn.close()
        print('on finish')