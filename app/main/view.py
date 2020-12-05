import json
import tornado.web
import pymysql
from app.main.action import IndexPostHandler

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        """
        根据安全cookie获取登录用户
        """
        return self.get_secure_cookie("user")

    def set_default_headers(self):
        """
        跨域请求头设置,所有业务处理类都要继承BaseHandler类
        """
        self.set_header("Access-Control-Allow-Origin", 'http://localhost:8080')
        # self.set_header("Content-type", '*')
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        # self.set_header("Access-Control-Max-Age", 1000)
    
    def options(self):
        """
        跨域非get请求，浏览器会发送一个OPTIONS请求,需要对这个请求做成功响应
        """
        self.set_status(204) # 这里的状态码一定要设置成功,200，201, 204等
        self.finish()

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
        ret_dict = {"ret": 0}
        if not self.current_user:
            ret_dict["ret"] = 1
        else:
            print("登录首页成功,当前登录用户: %s" % self.current_user.decode("utf-8"))
            ret_dict["user"] = tornado.escape.xhtml_escape(self.current_user)
        self.write(json.dumps(ret_dict))

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



class ForgetPasswordHandler(BaseHandler):

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