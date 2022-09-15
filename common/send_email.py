import yagmail

def send_mail(report, content='测试通过！！！请查看附件', to=['yyy333567@163.com']):
    """
    :param to: 收件人
    :param report: 附件地址
    :param content: 正文
    :return:
    """
    # MAIL_HOST = smtp.qq.com
    # MAIL_PORT = 465
    # MAIL_USERNAME = 280357392 @ qq.com
    # MAIL_PASSWORD = eyrukjuzcyuobijc
    # MAIL_ENCRYPTION = ssl
    yag = yagmail.SMTP(user='280357392@qq.com',
                       port=465,
                       password='exejkifrrfohbgce',
                       host='smtp.qq.com')
    subject = '接口自动化测试报告' # 主题
    yag.send(to, subject, content, report)