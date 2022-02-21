import time

import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_get_cookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        time.sleep(20)

        cookie = self.driver.get_cookies()
        with open('../conf/cookie.yaml', 'w') as f:
            yaml.safe_dump(cookie,f)
