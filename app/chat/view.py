from app.main.view import BaseHandler
import tornado.websocket
from datetime import datetime


class WebSocketBaseHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True


class ChatHandler(WebSocketBaseHandler):
    user_list = list()
    def initialize(self):
        print("func: initialize")
        pass
    
    # def prepare(self, *args, **kwargs):
    #     print("func: prepare")
    #     pass

    def open(self):
        # user_list = list()
        if self.current_user:  # 当能获取到用户信息,将用户放入列表中
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user = self.current_user.encode("utf-8")
            self.user_list.append(self)
            print("当前连接过来的用户名: %s" % user)
            for u in self.user_list:
                u.write_message("[%s]欢迎: %s 进入群聊" % (now_str, user))

    def on_close(self):
        print("func: on_close")

    def on_message(self, message):
        print("收到客户端消息: %s" % message)
        if self.current_user:
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user = self.current_user.encode("utf-8")
            for u in self.user_list:
                u.write_message("[%s] %s: %s" % (now_str, user, message))
