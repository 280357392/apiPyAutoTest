import pytest
from config import RunConfig
from apis._1_home.sign_in_api import SigInApi
from common.parse_data import parse_csv


@pytest.mark.skipif('_1_home' in RunConfig.skip_module, reason="跳过的模块")
@pytest.mark.run(order=1)
class TestSignInApi(object):

    @pytest.mark.parametrize(
        'city,status',  # 列
        parse_csv('test_login.csv'),
        ids=[  # 行
            '1.搜索存在的城市。',
            '2.搜索不存在的城市。',
        ]
    )
    # @pytest.mark.skipif(RunConfig.debug, reason="debug模式跳过用例")
    def test_search(self, city, status):
        """
        搜索某个城市的天气
        预期：
        1.搜索存在的城市，返回正确的数据。
        2.搜索不存在的城市，返回错误提示。
        """
        api = SigInApi(city)
        if status == '1':
            # 以有效城市进行搜索
            api.print_url()
            print('✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈')
            api.print_json_text()
            assert 200 == api.get_status_code()
            assert city == api.get_city()
            assert api.get_data()
        # hamcrest 第三方断言库。

        if status == '0':
            # 以失效城市进行搜索。
            api.print_url()
            print('✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈')
            api.print_json_text()
            assert 200 == api.get_status_code()
            assert 1001 == api.get_errcode(), f'期望errcode的值为：1001，实际errcode的值为：{api.get_errcode()}'

    pass
