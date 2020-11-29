from app.main.view import BaseHandler
import tornado.websocket


class WebSocketBaseHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True


class ChatHandler(WebSocketBaseHandler, BaseHandler):
    # def initialize(self):
    #     print("func: initialize")
    #     pass
    #
    def prepare(self, *args, **kwargs):
        print("func: prepare")
        pass

    def open(self):
        print("func: open")
        user_name = self.current_user
        name = self.get_secure_cookie("user")
        print(name)
        self.write_message("欢迎: %s 进入群聊" % user_name)

    def on_close(self):
        print("func: on_close")

    def on_message(self, message):
        print("you said: %s" % message)
        print("func: on_message")

    # def get(self, *args, **kwargs):
    #     print("get ")
    #     self.write("get")
    #     pass
    #
    # def post(self, *args, **kwargs):
    #     self.write("post")
    #     pass
    #
    # def put(self, *args, **kwargs):
    #     self.write("put")
    #     pass
    #
    # def head(self, *args, **kwargs):
    #     self.write("head")
    #     pass
    #
    # def delete(self, *args, **kwargs):
    #     self.write("delete")
    #     pass
    #
    # def option(self, *args, **kwargs):
    #     self.write("option")
    #     pass

    # def on_finish(self):
    #     print("on_finsh")