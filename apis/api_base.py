import json
from urllib.parse import unquote

import requests

from config import RunConfig
from common.pring_info import print_reques


class ApiBase:
    """
        api公共方法
    """

    def __init__(self):
        self.base_url = RunConfig.base_url
        self.token = RunConfig.token
        self._response: requests.Response = None

    def get_status_code(self) -> int:
        """
        获取响应状态码.
        """
        return self._response.status_code

    def get_json_text(self) -> str:
        """
        获取响应的内容。
        """
        return json.dumps(self._response.json(), indent=2, ensure_ascii=False)

    def get_text(self) -> str:
        """
        获取响应的内容。
        """
        return self._response.text

    def get_response_headers(self):
        """
        获取响应头。
        """
        return self._response.headers

    def get_request_headers(self):
        """
        获取请求头。
        """
        return self._response.request.headers

    def get_url(self):
        """
        获取url
        """
        return self._response.url

    def print_info(self):
        """
        打印数据，格式：
        GET url
        headers: {...}
        body:
        None
        {.....}
        """
        if RunConfig.debug:
            # 调试模式
            print('✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈request✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈')
            print('{}\r\nheaders: {}\r\nbody:\r\n{}'.format(
                self._response.request.method + ' ' + unquote(self._response.request.url),
                self._response.request.headers, self._response.request.body))
            print('✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈response✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈')
            print(self._response.text)
        else:
            picnic_items = {
                'url:': unquote(self._response.request.url),
                'method:': self._response.request.method,
                'request_headers:': str(self._response.request.headers)[0:100] + "...",
                'request_body:': str(self._response.request.body)[0:100] + "...",
                'response_body:': self._response.text[0:100] + "..."}
            print_reques(picnic_items, 27, 60)
