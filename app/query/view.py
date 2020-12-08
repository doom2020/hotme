import tornado.httpclient


class QueryHandler(object):

    def fun1(self):
        """
        http同步请求
        """
        http_client = tornado.httpclient.HTTPClient()
        try:
            response = http_client.fetch("www.baidu.com")
            print(response.body)
        except tornado.httpclient.HTTPError as e:
            print("error: %s" % e)
        except Exception as e:
            print("error: %s" % e)
        http_client.close()
