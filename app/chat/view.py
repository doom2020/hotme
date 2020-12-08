import tornado.websocket
from datetime import datetime
from app.main.view import BaseHandler



class WebSocketBaseHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        """
        跨域请求处理
        """
        return True


class ChatHandler(WebSocketBaseHandler):
    client_list = []
    def open(self):
        now_str_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("[%s]建立连接: %s" % (now_str_time, self))
        self.client_list.append(self)
        for c in self.client_list:
            c.write_message("[%s]系统消息: %s 进入群聊" % (now_str_time, self))

    def on_close(self):
        now_str_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("[%s]断开连接: %s" % (now_str_time, self))
        self.client_list.remove(self)
        for c in self.client_list:
            c.write_message("[%s]系统消息: %s 离开群聊" % (now_str_time, self))

    def on_message(self, message):
        now_str_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("[%s]收到客户端: %s 消息: %s" % (now_str_time, self, message))
        for c in self.client_list:
            c.write_message("[%s] %s说: %s" % (now_str, self, message))
