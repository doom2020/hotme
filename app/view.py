import hashlib
import json

import tornado.web
import pymysql
from tornado.escape import json_decode

from utils.conn import Base, session
from app.models import *
from app.action import LoginOperation


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
        # print(json.loads(self.request.body))
        print("post 请求")
        login_operation = LoginOperation(self)
        op_handle = login_operation.get_handler()
        # self.write('登录post请求')

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

    @staticmethod
    def md5(the_str):
        return hashlib.md5(the_str.encode('utf8')).hexdigest()

    def prepare(self):
        # if self.request.headers['Content-Type'] == 'application/json':
        #     self.args = json_decode(self.request.body)
        # data_type = self.request.headers.get("Content-Type")
        # if "application/json" in data_type:
        #     json_data = json.loads(self.request.body)
        #     # print('222222222222222222222')
        #     # print(aa)
        #     # print(self.kwargs)
        # print(data_type)
        # print(json_data)
        # self.kwargs = json.loads(self.request.body)
        print('this is a prepare')

    def get(self, *args, **kwargs):
        self.render('register.html')

    def post(self, *args, **kwargs):
        json_data = json.loads(self.request.body)
        post_type = json_data['post_type']
        print(post_type)
        handle = None
        if hasattr(RegisterHandler, post_type):
            handle = getattr(RegisterHandler, post_type)
        if handle:
            ret_dict = handle(json_data)
        print(ret_dict)
        self.write(ret_dict)

    def on_finish(self):
        if self.conn:
            self.conn.close()
        print('on finish')

    @staticmethod
    def check_account(json_data):
        ret_dict = {'ret': 0, 'data': ''}
        account = json_data['account']
        user_info_objs = session.query(UserInfo).filter(UserInfo.name == account, UserInfo.is_delete == 0).all()
        if user_info_objs:
            ret_dict['ret'] = 1
        return ret_dict

    @staticmethod
    def check_phone(json_data):
        ret_dict = {'ret': 0, 'data': ''}
        phone = json_data['phone']
        user_info_objs = session.query(UserInfo).filter(UserInfo.phone == phone, UserInfo.is_delete == 0).all()
        if user_info_objs:
            ret_dict['ret'] = 1
        return ret_dict

    @staticmethod
    def register(json_data):
        ret_dict = {'ret': 0, 'data': ''}
        account = json_data['account']
        phone = json_data['phone']
        upwd = json_data['upwd']
        cpwd = json_data['cpwd']
        secret_upwd = RegisterHandler.md5(upwd)
        user_info_obj = UserInfo(name=account, phone=phone, password=secret_upwd, is_delete=0)
        session.add(user_info_obj)
        session.commit()
        return ret_dict



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
        session.close()
        if self.conn:
            self.conn.close()
        print('on finish')