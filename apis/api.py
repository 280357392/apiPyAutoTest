from config import RunConfig
import requests
import json


class Api(object):

    def __init__(self):
        self._base_url = RunConfig.base_url
        self._headers = {
            'Content-Type': 'application/json;',
            'User-Agent': 'Mozilla/5.0'
        }

    def _set_headers(self, **kwargs):
        """
        构建请求头，在原有的基础上更新或新增请求头。\n
        调用方式:\n
            new_headers = {'key': 'value'} \n
            set_headers(**new_headers) \n
            set_headers(token='123456') \n
        """
        self._headers.update(kwargs)

    def _get(self, url, params=None, headers=None, auth=None, timeout=10) -> requests.Response:
        """
        get请求。
        """
        if headers is None:
            headers = self._headers

        return requests.get(
            url=url,
            params=params,
            headers=headers,
            auth=auth,
            timeout=timeout,
        )

    def _post(self, url, data, headers=None, auth=None, timeout=10) -> requests.Response:
        """
        post请求。
        """
        if headers is None:
            headers = self._headers

        return requests.post(
            url=url,
            json=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
        )

    def _upload(self, url, file, headers=None) -> requests.Response:
        """
        上传文件。\n
        """
        if headers is None:
            headers = self._headers
        return requests.post(
            url=url,
            headers=headers,
            files={
                "file": ('wx.jpg', open(file, 'rb'), "image/jpeg", {})
            },
        )

    def get_status_code(self) -> int:
        """
        获取响应状态码.
        """
        return self._response.status_code

    def print_json_text(self) -> str:
        """
        打印获取响应的内容。
        """
        print(json.dumps(self._response.json(), indent=2, ensure_ascii=False))

    def get_headers(self):
        """
        获取响应头。
        """
        return self._response.headers

    def print_url(self):
        """
        获取url
        """
        print(self._response.url)