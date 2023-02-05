from apis.api_base import ApiBase
from apis.api_info import ApiInfo
from apis.controller.api_controller_base import ApiControllerBase
from apis.controller.api_controller_v1 import ApiControllerV1


class SigInApi(ApiBase):

    def __init__(self, city, **kwargs):
        """
        1.设置接口请求头。
        2.发送接口请求。
        """
        super().__init__()
        self.api_controller = ApiControllerV1()
        self.__set_headers(self.api_controller, **kwargs)
        self.__set_headers(self.api_controller, **ApiInfo.sig_in_api['headers'])
        self.__set_headers(self.api_controller, token=self.token)
        self.__send_request(self.api_controller, city)

    def __set_headers(self, api_controller, **kwargs):
        """
        设置请求头
        """
        if isinstance(api_controller, ApiControllerBase):
            api_controller.set_headers(**kwargs)
        else:
            raise ValueError(api_controller.__class__.__name__, '必须是ApiControllerBase类的子类。')

    def __get_url(self, city):
        """
        构建url
        """
        url = ApiInfo.sig_in_api['url'].format(city)
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
    api = SigInApi('北京')  # 设置参数，使用默认请求头发送请求。
    # api = SigInApi(ApiControllerV1(), '北京', token1='123456', token2='789')  # 添加请求头方式1。
    # api = SigInApi(ApiControllerV1(), '北京', **{'token2': '333', 'token4': '444'})  # # 添加请求头方式2。
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
    pass
