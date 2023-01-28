import pytest
from py.xml import html

from apis.controller.api_controller_v1 import ApiControllerV1
from apis.order_1_home.log_api import LogApi
from config import RunConfig


def pytest_html_report_title(report):
    report.title = "接口自动化测试报告"


def pytest_configure(config):
    # 移除所有Environment项目。
    config._metadata = {}
    # 添加Environment项
    config._metadata["版本信息"] = "v1.0"
    config._metadata["项目名称"] = "API数据接口"
    config._metadata["运行环境信息"] = "自动化测试环境"


# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试中心")])
    prefix.extend([html.p("测试人员: 蒙伟")])


# 设置用例描述表头
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.pop()  # 移除links


# 设置用例描述表格
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()  # 移除links

    # def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的name和nodeid的中文显示在控制台上
    解决终端日志中文乱码
    """
    # for i in items:
    #     i.name = i.name.encode("utf-8").decode("unicode_escape")
    #     i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


# @pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    # if report.when == 'call' or report.when == "setup":
    # 用例结束后才执行1次
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 测试失败时
            # ...
            pass
        # 无论是否失败都截图
        # ...
    report.extra = extra
    # 再把编码改回来，解决报告中文乱码问题。
    # report.nodeid = report.nodeid.encode("unicode_escape").decode("utf-8")


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


@pytest.fixture(scope='session', autouse=True)
def start():
    # print('测试开始---------->')
    # 测试开始前执行一次
    # 测试开始前获取token
    RunConfig.token = str(LogApi(ApiControllerV1(),'username','pwd').get_token())
    yield


@pytest.fixture(scope="session", autouse=True)
def stop():
    yield
    # print(RunConfig.token)
    # 执行退出登录操作
    # print('测试结束---------->')
