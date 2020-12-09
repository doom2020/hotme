import tornado.httpclient
from app.main.view import BaseHandler
import time
from tornado import gen


class QueryHandler(BaseHandler):

    # async def get(self, *args, **kwargs):
    #     """
    #     异步请求
    #     """
    #     http_client = tornado.httpclient.AsyncHTTPClient()
    #     try:
    #         response = await http_client.fetch("http://www.douban.com")
    #     except Exception as e:
    #         print("error: %s" % e)
    #     else:
    #         print(response.body)
    #     self.write(response.body)

    # def get(self, *args, **kwargs):
    #     """
    #     http同步请求
    #     """
    #     http_client = tornado.httpclient.HTTPClient()
    #     try:
    #         response = http_client.fetch("http://www.douban.com")
    #         print(response.body)
    #     except tornado.httpclient.HTTPError as e:
    #         print("error: %s" % e)
    #     except Exception as e:
    #         print("error: %s" % e)
    #     http_client.close()
    #     self.write(response.body)
    # @gen.coroutine
    # def get(self):
    #     """
    #     基于生成器的协程
    #     """
    #     http_client = tornado.httpclient.AsyncHTTPClient()
    #     response = yield http_client.fetch("http://www.douban.com")
    #     print(response.body)
    #     self.write(response.body)

    @gen.coroutine
    def get(self):
        """
        生成器协程多任务并发
        """
        http_client = tornado.httpclient.AsyncHTTPClient()
        response1, response2 = yield [http_client.fetch('http://www.baidu.com'), http_client.fetch('http://www.google.com')]
        print(response1)
        print(response2)
    
