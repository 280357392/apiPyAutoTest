import json
import requests
from urllib.parse import unquote

from common.mysql_db import MysqlDB
from config import RunConfig
from common.pring_info import print_reques


class BaseApi:
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
        打印数据
        """
        request_body = self._response.request.body
        if type(request_body) == bytes:
            request_body = str(request_body, 'utf-8').encode('utf-8').decode('unicode_escape')
        else:
            request_body = str(request_body).encode('utf-8').decode('unicode_escape')
        if RunConfig.debug:
            # 调试模式
            print('✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈request✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈')
            print('{}\r\nrequest_headers: {}\r\nrequest_body: {}'.format(
                self._response.request.method + ' ' + unquote(self._response.request.url),
                self._response.request.headers, request_body))
            print('✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈response✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈')
            print(self._response.text)
        else:
            picnic_items = {
                'url:': unquote(self._response.request.url),
                'method:': self._response.request.method,
                'request_headers:': str(self._response.request.headers)[0:100] + "...",
                'request_body:': request_body[0:100] + "...",
                'response_body:': self._response.text[0:100] + "..."}
            print_reques(picnic_items, 27, 60)

    @staticmethod
    def read_data(sql, args=None):
        """
        查询数据库

        :param sql: 查询语句
        :param args: 条件列表[]
        :return: 查询成功时返回一列数据（元组），否则报错。
        """
        db = MysqlDB()
        data = db.retrieve(sql, args)
        db.close_db()
        if data:
            return data
        else:
            assert False, '数据库未查询到相关数据。'

