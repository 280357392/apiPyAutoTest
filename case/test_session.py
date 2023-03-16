import pytest

from config import RunConfig
from apis.session.login_api import LoginApi


@pytest.mark.skipif('test_session.py' in RunConfig.skip_module, reason="跳过该模块")
@pytest.mark.run(order=1)
class TestSession(object):
    """
    session模块
    """

    # @pytest.mark.skipif(RunConfig.debug, reason="debug模式时将跳过该用例")
    def test_log_api(self):
        data = LoginApi.read_data("select classid,name from student where classid = %s;", [13])
        la = LoginApi(data[0], data[1])
        la.print_info()
        assert 1001 == la.get_errcode(), f'期望errcode的值为：1001，实际errcode的值为：{la.get_errcode()}'
