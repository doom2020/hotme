import os
import tornado.web
import tornado.ioloop
from tornado.options import define, options
from app.view import IndexHandler, LoginHandler, RegisterHandler, CreateTableHandler, DeleteTableHandler, \
    ForgetPasswordHandler

DEBUG = True

if DEBUG:
    define("port", default=8000, type=int, help="port to listen on")
    define("db_host", default="127.0.0.1", help="hotme database host")
    define("db_port", default=3306, help="hotme database port")
    define("db_database", default="hotme", help="hotme database name")
    define("db_user", default="root", help="hotme database user")
    define("db_password", default='123456', help="hotme database password")
else:
    define("port", default=8080, type=int, help="port to listen on")
    define("db_host", default="127.0.0.1", help="hotme database host")
    define("db_port", default=3306, help="hotme database port")
    define("db_database", default="hotme", help="hotme database name")
    define("db_user", default="root", help="hotme database user")
    define("db_password", default='123456', help="hotme database password")


def make_app():
    return tornado.web.Application([
        (r"/create_table/", CreateTableHandler),
        (r"/delete_table/", DeleteTableHandler),
        (r"/", IndexHandler),
        (r"/login/", LoginHandler),
        (r"/register/", RegisterHandler),
        (r"/forget_password/", ForgetPasswordHandler)
    ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        xsrf_cookies=False,
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        login_url="/login/",
        debug=True,

    )

if __name__ == "__main__":
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()