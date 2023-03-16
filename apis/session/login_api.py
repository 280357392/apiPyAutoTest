import json

from ..base_controller import BaseController
from ..v1_controller import V1Controller
from apis.base_api import BaseApi
from apis.api_info import Session


class LoginApi(BaseApi):

    def __init__(self, username, pwd, **kwargs):
        super().__init__()
        self.controller = V1Controller()
        self.__set_headers(self.controller, **kwargs)
        self.__set_headers(self.controller, **Session.login_api['headers'])
        self.__send_request(self.controller, username, pwd)

    def __set_headers(self, controller, **kwargs):
        """
        设置请求头
        """
        if isinstance(controller, BaseController):
            controller.set_headers(**kwargs)
        else:
            raise ValueError(controller.__class__.__name__, '必须是BaseController的子类。')

    def __get_url(self):
        """
        拼接url
        """
        url = Session.login_api['url']
        return ''.join([self.base_url, url])

    def __get_data(self, username, pwd):
        """
        构造请求参数-字典
        """
        data = Session.login_api['data'] % (username, pwd)
        return json.loads(data)

    def __send_request(self, controller, username, pwd):
        self._response = controller.post(url=self.__get_url(), data=self.__get_data(username, pwd))

    def get_token(self):
        return self._response.json().get('token')

    def get_errcode(self) -> int:
        return self._response.json().get('errcode')


if __name__ == '__main__':
    api = LoginApi('zs123', '123456')
    print(api.get_text())
