import json

class IndexPostHandler:
    def __init__(self, request):
        self.request = request

    def get_handler(self):
        info = json.loads(self.request.request.body)
        post_type = info.get('post_type', '')
        index_post_cool = IndexPostCool(self.request)
        handle = None
        if post_type and hasattr(index_post_cool, post_type):
            handle = getattr(index_post_cool, post_type)
        return handle

class IndexPostCool:
    def __init__(self, request):
        self.request = request

    def func1(self):
        ret_dict = {"ret": 0, "data": ''}
        return ret_dict

    def func2(self):
        ret_dict = {"ret": 0, "data": ''}
        return ret_dict

    def func3(self):
        ret_dict = {"ret": 0, "data": ''}
        return ret_dict
