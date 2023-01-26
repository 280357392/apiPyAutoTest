import json

from apis.api import Api
from apis.urls import Urls


class LogApi(Api):

    def __init__(self, username, pwd, **kwargs):
        super().__init__()
        self._set_headers(**kwargs)
        self._set_headers(**Urls.log_api['headers'])
        self.__send_request(username, pwd)

    def __get_url(self):
        url = Urls.log_api['url']
        return ''.join([self._base_url, url])

    def __get_data(self, username, pwd):
        data = Urls.log_api['data'] % (username, pwd)
        return json.loads(data)

    def __send_request(self, username, pwd):
        self._response = self._post(url=self.__get_url(), data=self.__get_data(username, pwd))

    def get_token(self):
        return self._response.json().get('token')


if __name__ == '__main__':
    api = LogApi('zs123', '123456')
    # print(api._response.request.headers)
    # print(api._response.request.body)
    # print(api.get_token())
    # print(type(api.get_token()))
    # print(type(api._response.request.body))
    # print(str(api._response.request.body))
    # print(api._response.request.body.decode())# 为空报错
    # print(str(api._response.request.body))
    pass
