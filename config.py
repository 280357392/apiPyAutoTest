from pathlib import Path


class RunConfig:
    """
    配置信息
    """

    debug = True
    """等于True时表示调试模式，将跳过全部用例。"""

    skip_module = [
        # '_1_home',
    ]
    """跳过的模块"""

    base_url = u"https://v0.yiketianqi.com"

    token = ''

    cases_path = str(Path.cwd() / 'test_cases')
    """测试用例的目录路径"""

    rerun = "0"
    """失败重跑次数（慎用，可能会错过缺陷）"""

    max_fail = "5"
    """当达到最大失败数，停止执行"""

    new_report = ""
    """测试报告目录（默认test_report，此处配置无效，无需修改"""
