from apis.api import Api


class SigInApi(Api):
    """
    接口地址：/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=
    """

    def __init__(self, city, **kwargs):
        super().__init__()
        self._set_headers(**kwargs)
        self.__send_request(city)

    def __send_request(self, city):
        self._response = self._get(url=self.__get_url(city))

    def __get_url(self, city):
        # 构建url
        url = '/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city={}'.format(city)
        return ''.join([self._base_url, url])

    def get_city(self):
        return self._response.json().get('city')

    def get_data(self):
        return self._response.json().get('data')

    def get_errcode(self) -> int:
        return self._response.json().get('errcode')


if __name__ == '__main__':
    # api = SigInApi('四川')
    # print(api.get_status_code())  # 获取响应状态码,200
    # print(api.get_headers())  # 打印请求头
    # print(api.get_city())  # 打印响应内容
    # print(api.get_data())
    # print(api.get_errcode())
    # api.print_json_text()
    # api.print_url()
    pass
