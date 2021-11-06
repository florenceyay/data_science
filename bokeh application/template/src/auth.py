import tornado
from tornado.web import RequestHandler

#18.220.254.181:8080/?username=nyc&password=iheartnyc

def get_user(request_handler):
    return request_handler.get_cookie("user")


login_url = '/'

class LoginHandler(RequestHandler):
    def set_current_user(self, user):
        if user:
            self.set_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")

    
    def get(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')      
        
        if username == 'nyc' and password == 'iheartnyc':
            print('AUTHENTIFICATION SUCCEEDED')
            self.set_current_user(username)
            self.redirect('/nyc_dash')
        else:
            print('AUTHENTIFICATION FAILED')
            self.redirect('/failed')
