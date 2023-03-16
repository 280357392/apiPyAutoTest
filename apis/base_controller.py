import requests

class BaseController(object):

    MESSAGE_1 = '子类必须重写该方法。'

    def __init__(self):
        self._headers = {
            'Content-Type': 'application/json;',
            'User-Agent': 'Mozilla/5.0'
        }

    def set_headers(self, **kwargs):
        """
        构建请求头，在原有的基础上更新或新增请求头。
        值不允许是int类型。
        调用方式:
            set_headers(**{'key': 'value'})
            set_headers(token='123456')
        """
        raise NotImplementedError(BaseController.MESSAGE_1)

    def get(self, url, params=None, headers=None, auth=None, timeout=10) -> requests.Response:
        """
        get请求。
        """
        raise NotImplementedError(BaseController.MESSAGE_1)

    def post(self, url, data, headers=None, auth=None, timeout=10) -> requests.Response:
        """
        post请求。
        """
        raise NotImplementedError(BaseController.MESSAGE_1)

    def upload(self, url, file, headers=None) -> requests.Response:
        """
        上传文件。
        """
        raise NotImplementedError(BaseController.MESSAGE_1)
