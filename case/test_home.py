import pytest

from config import RunConfig
from apis.home.check_weather_api import CheckWeatherApi
from common.parse_data import parse_csv


@pytest.mark.skipif('test_home.py' in RunConfig.skip_module, reason="跳过该模块")
@pytest.mark.run(order=2)
class TestHome(object):
    """
    home模块
    用例之间不允许相互依赖。
    用例执行顺序是按方法定义的顺序决定的，跟名称无关。
    """

    @pytest.mark.parametrize(
        'city,status',  # 列名
        # parse_csv('test_search.csv'),
        # 2行数据
        [
            ('广州', 1),
            ('美国', 2)
        ],
        # 提示信息
        ids=[
            '1.输入正确的参数（存在的城市），应返回正确的数据。',
            '2.输入错误的参数（不存在的城市），应返回正确的错误提示。',
        ]
    )
    # @pytest.mark.skipif(RunConfig.debug, reason="debug模式时将跳过该用例")
    def test_check_weather(self, city, status):
        """
        搜索某个城市的天气
        预期：
        1.输入正确的参数（存在的城市），应返回正确的数据。
        2.输入错误的参数（不存在的城市），应返回正确的错误提示。
        """
        cwa = CheckWeatherApi(city)
        cwa.print_info()

        if status == 1:
            # 以有效参数进行测试
            assert 200 == cwa.get_status_code()
            assert city == cwa.get_city()
            assert cwa.get_data('data')
            # hamcrest 第三方断言库。
        elif status == 2:
            # 以无效参数进行测试
            assert 200 == cwa.get_status_code()
            assert 1001 == cwa.get_errcode(), f'期望errcode的值为：1001，实际errcode的值为：{cwa.get_errcode()}'
