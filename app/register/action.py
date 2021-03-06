import json
from app.common.models import *
import hashlib
from utils.conn import session
from tools import md5Str


class RegisterPostHandler:
    def __init__(self, request):
        self.request = request

    def get_handler(self):
        info = json.loads(self.request.request.body)
        post_type = info['post_type']
        register_post_cool = RegisterPostCool(self.request)
        handle = None
        if post_type and hasattr(register_post_cool, post_type):
            handle = getattr(register_post_cool, post_type)
        return handle



class RegisterPostCool:
    def __init__(self, request):
        self.request = request
        self.info = json.loads(self.request.request.body)

    def check_account(self):
        ret_dict = {'ret': 0, 'data': ''}
        account = self.info['account']
        user_info_objs = session.query(UserInfo).filter(UserInfo.name == account, UserInfo.is_delete == 0).all()
        if user_info_objs:
            ret_dict['ret'] = 1
        return ret_dict

    def check_phone(self):
        ret_dict = {'ret': 0, 'data': ''}
        phone = self.info['phone']
        user_info_objs = session.query(UserInfo).filter(UserInfo.phone == phone, UserInfo.is_delete == 0).all()
        if user_info_objs:
            ret_dict['ret'] = 1
        return ret_dict

    def register(self):
        ret_dict = {"ret": 0, "data": ''}
        account = self.info['account']
        phone = self.info['phone']
        upwd = self.info['upwd']
        cpwd = self.info['cpwd']
        secret_upwd = md5Str(upwd)
        user_info_obj = UserInfo(name=account, phone=phone, password=secret_upwd, is_delete=0)
        session.add(user_info_obj)
        try:
            session.commit()
            result = self.request.set_secure_cookie("user", account, expires_days=10)  # 这里可以看看源码设置好cookie是否有返回值
            if result:
                print("注册成功,设置的cookie: %s" % self.request.get_secure_cookie("user"))
            else:
                print("注册成功,设置cookie失败")
            ret_dict["user"] = account
        except Exception as e:
            ret_dict['ret'] = 1
            session.rollback()
        finally:
            session.close()
            return ret_dict

    
