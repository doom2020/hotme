import json
import hashlib
from app.common.models import *
from utils.conn import session
from tools import md5Str


class LoginPostHandler:
    def __init__(self, request):
        self.request = request

    def get_handler(self):
        info = json.loads(self.request.request.body)
        print('1111111111111')
        print(info)
        post_type = info['post_type']
        login_post_cool = LoginPostCool(self.request)
        handle = None
        if post_type and hasattr(login_post_cool, post_type):
            handle = getattr(login_post_cool, post_type)
        return handle


class LoginPostCool:
    def __init__(self, request):
        self.request = request
        self.info = json.loads(self.request.request.body)

    def login(self):
        ret_dict = {'ret': 0, 'data': ''}
        account = self.info['account']
        password = self.info['password']
        if not account or not password:
            ret_dict['ret'] = 1
            return ret_dict
        secret_pwd = md5Str(password)
        try:
            user_info_obj = session.query(UserInfo).filter(UserInfo.name == account, UserInfo.password == secret_pwd, UserInfo.is_delete == 0).one()
        except Exception as e:
            ret_dict['ret'] = 2
            return ret_dict
        return ret_dict