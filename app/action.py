class LoginOperation:
    def __init__(self, request):
        self.request = request

    def get_handler(self):
        post_type = self.request.request.body
        print('1111111111111111')
        print(post_type)