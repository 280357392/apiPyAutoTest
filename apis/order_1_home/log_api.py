import json
from apis.controller.api_controller_base import ApiControllerBase
from apis.controller.api_controller_v1 import ApiControllerV1
from apis.api_base import ApiBase
from apis.api_info import ApiInfo


class LogApi(ApiBase):

    def __init__(self, api_controller, username, pwd, **kwargs):
        super().__init__()
        self.__set_headers(api_controller, **kwargs)
        self.__set_headers(api_controller, **ApiInfo.log_api['headers'])
        self.__send_request(api_controller, username, pwd)

    def __set_headers(self, api_controller, **kwargs):
        """
        设置请求头
        """
        if isinstance(api_controller, ApiControllerBase):
            api_controller.set_headers(**kwargs)
        else:
            raise ValueError(api_controller.__class__.__name__, '必须是ApiControllerBase类的子类。')

    def __get_url(self):
        """
            拼接字符串
        """
        url = ApiInfo.log_api['url']
        return ''.join([self.base_url, url])

    def __get_data(self, username, pwd):
        data = ApiInfo.log_api['data'] % (username, pwd)
        return json.loads(data)

    def __send_request(self, api_controller, username, pwd):
        self._response = api_controller.post(url=self.__get_url(), data=self.__get_data(username, pwd))

    def get_token(self):
        return self._response.json().get('token')

    def get_errcode(self) -> int:
        return self._response.json().get('errcode')


if __name__ == '__main__':
    api = LogApi(ApiControllerV1(), 'zs123', '123456')
    print(api.get_text())
    pass
