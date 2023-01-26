import pytest

from apis.order_1_home.log_api import LogApi
from config import RunConfig
from apis.order_1_home.sign_in_api import SigInApi
from common.parse_data import parse_csv


@pytest.mark.skipif('order_1_home' in RunConfig.skip_module, reason="跳过的模块")
@pytest.mark.run(order=1)
class TestOrder1Home(object):
    """
    用例之间不允许相互依赖。
    用例执行顺序是按方法定义的顺序决定的，跟名称无关。
    """

    @pytest.mark.parametrize(
        'city,status',  # 2列
        # parse_csv('test_search.csv'),
        # 2行
        [
            ('广州', '1'),
            ('四川', '0')
        ],
        ids=[  # 2行提示信息
            '1.输入正确的参数（存在的城市），应返回正确的数据。',
            '2.输入错误的参数（不存在的城市），应返回正确的错误提示。',
        ]
    )
    @pytest.mark.skipif(RunConfig.debug, reason="debug模式时跳过用例")
    def test_sign_in_api(self, city, status):
        """
        搜索某个城市的天气
        预期：
        1.输入正确的参数（存在的城市），应返回正确的数据。
        2.输入错误的参数（不存在的城市），应返回正确的错误提示。
        """
        api = SigInApi(city)

        # 以有效参数进行测试
        if status == '1':
            api.print_info()
            assert 200 == api.get_status_code()
            assert city == api.get_city()
            assert api.get_data('data')
            # hamcrest 第三方断言库。

        # 以无效参数进行测试
        if status == '0':
            api.print_info()
            assert 200 == api.get_status_code()
            assert 1001 == api.get_errcode(), f'期望errcode的值为：1001，实际errcode的值为：{api.get_errcode()}'

        pass

    @pytest.mark.skipif(RunConfig.debug, reason="debug模式时跳过用例")
    def test_log_api(self):
        api = LogApi('zs123', '123456')  # 必须
        api.print_info()  # 必须
        assert 200 == api.get_status_code()  # 必须
        pass

