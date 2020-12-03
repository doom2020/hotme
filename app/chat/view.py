from app.main.view import BaseHandler
import tornado.websocket


class WebSocketBaseHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True


class ChatHandler(WebSocketBaseHandler):
    def initialize(self):
        print("func: initialize")
        pass
    
    # def prepare(self, *args, **kwargs):
    #     print("func: prepare")
    #     pass

    def open(self):
        if self.current_user:
            user = self.current_user.encode("utf-8")
        else:
            user = '未知用户'
        print("当前连接过来的用户: %s" % user)
        self.write_message("欢迎: %s " % user)

    def on_close(self):
        print("func: on_close")

    def on_message(self, message):
        print("收到客户都消息: %s" % message)
