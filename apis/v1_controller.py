import requests

from .base_controller import BaseController


class V1Controller(BaseController):

    def set_headers(self, **kwargs):
        self._headers.update(kwargs)

    def get(self, url, params=None, headers=None, auth=None, timeout=10):
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

    def post(self, url, data, headers=None, auth=None, timeout=10):
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

    def upload(self, url, file, headers=None):
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

