import os
import tornado.web
import tornado.ioloop
from tornado.options import define, options
from app.view import IndexHandler, LoginHandler, RegisterHandler, CreateTableHandler, DeleteTableHandler

define("port", default=8080, type=int, help="port to listen on")


def make_app():
    return tornado.web.Application([
        (r"/create_table/", CreateTableHandler),
        (r"/delete_table/", DeleteTableHandler),
        (r"/", IndexHandler),
        (r"/login/", LoginHandler),
        (r"/register/", RegisterHandler)
    ],
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    static_path=os.path.join(os.path.dirname(__file__), 'static')
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()