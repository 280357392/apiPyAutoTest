class Home:
    """home模块接口信息"""

    check_weather = {
        'module': 'order_1_home',
        'title': '某某接口',
        'method': 'get',
        'headers': {
            'device': 'android'
        },
        'url': '/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city={}',
    }


class Session:
    """session模块。
    登录注册等接口信息。"""

    login_api = {
        'module': 'order_1_home',
        'title': '某某接口',
        'method': 'post',
        'headers': {
            'device': 'ios'
        },
        'url': '/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city={}',
        'data': '{"username": "%s", "pwd":"%s"}'
    }
