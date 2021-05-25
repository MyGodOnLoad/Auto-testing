import time

from selenium import webdriver


def login():
    b = webdriver.Chrome()
    b.get('http://energy-micro.enesource.cn')
    time.sleep(5)
    b.find_element_by_id('username').send_keys('zhangbin')
    b.find_element_by_id('password').send_keys('zb123456')
    b.find_element_by_id('loginButton').click()
    time.sleep(5)


if __name__ == '__main__':
    login()
