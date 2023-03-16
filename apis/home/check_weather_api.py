from apis.base_api import BaseApi
from apis.api_info import Home
from ..base_controller import BaseController
from ..v1_controller import V1Controller


class CheckWeatherApi(BaseApi):

    def __init__(self, city, **kwargs):
        """
        1.设置接口请求头。
        2.发送接口请求。
        """
        super().__init__()
        self.controller = V1Controller()
        self.__set_headers(self.controller, **kwargs)
        self.__set_headers(self.controller, **Home.check_weather['headers'])
        self.__set_headers(self.controller, token=self.token)
        self.__send_request(self.controller, city)

    def __set_headers(self, controller, **kwargs):
        """
        设置请求头
        """
        if isinstance(controller, BaseController):
            controller.set_headers(**kwargs)
        else:
            raise ValueError(controller.__class__.__name__, '必须是BaseController的子类。')

    def __get_url(self, city):
        """
        构建url
        """
        url = Home.check_weather['url'].format(city)
        return ''.join([self.base_url, url])

    def __send_request(self, api_controller, city):
        """
        发送请求
        """
        self._response = api_controller.get(url=self.__get_url(city))

    def get_city(self):
        return self._response.json().get('city')

    def get_data(self, key):
        return self._response.json().get(key)

    def get_errcode(self) -> int:
        return self._response.json().get('errcode')


if __name__ == '__main__':
    api = CheckWeatherApi('北京')  # 设置参数，使用默认请求头发送请求。
    # api = CheckWeatherApi(V1Controller(), '北京', token1='123456', token2='789')  # 添加请求头方式1。
    # api = CheckWeatherApi(ApiControllerV1(), '北京', **{'token2': '333', 'token4': '444'})  # # 添加请求头方式2。
    # print(api.get_status_code())  # 获取响应状态码,200
    print(str(api.get_request_headers()))  # 打印请求头
    # print(api.get_response_headers())  # 打印响应头
    # print(api.get_city())  # 获取指定数据1
    # print(api.get_data('data')) # 获取指定数据2
    # print(api.get_errcode()) # 获取错误响应码。
    # print(api.get_json_text()) # 打印响应内容（json格式）
    # print(api.get_url()) # 打印url
    # print(api._response.request.headers)
    # print(type(api._response.request.body))
