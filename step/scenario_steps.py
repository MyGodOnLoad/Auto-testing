# file_name: scenario_steps.py
import time

import pytest
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from config.settings import BaseUrl


@pytest.fixture
@given(parsers.parse("用户:{username}, 密码:{password}"))
def user(username, password):  # 类似一个pytest的fixture方法, 其他步骤可以使用其返回值
    return dict(username=username, password=password)


# @given(parsers.parse("分类:{category},标题:{title},描述:{description}"))
# def course(category, title, description):
#     return dict(category=category, title=title, description=description)


# @when("登录educa后台")  # 固定操作,不需要获取参数则不用parsers.parse()
# def login(selenium, user):  # 使用上面user函数的返回数据, selenium为浏览器driver(来着:pytest-selenium)
#     selenium.get("http://qaschool.cn:8000/admin/")
#     selenium.find_element_by_id("id_username").send_keys(user['username'])
#     selenium.find_element_by_id("id_password").send_keys(user['password'])
#     selenium.find_element_by_class_name("submit-row").click()


# @when(parsers.parse("点击:{module}模块->点击新增按钮"))
# def add_course(selenium, module):
#     selenium.find_element_by_link_text(module).click()  # 点击'Courses'链接
#     selenium.find_element_by_class_name("addlink").click()  # 点击'新增 COURSE'按钮
#
#
# @when("作者选择当前<用户>,选择<分类>,输入<标题>,<描述>,点击保存")  # 也可以不使用<>, 要与场景中一致, 使用<>只是提示是从Given的数据中获取
# def edit_course(selenium, user, course):  # 使用上面course函数的返回数据
#     Select(selenium.find_element_by_id("id_owner")).select_by_visible_text(user['username'])  # 选择作者
#     Select(selenium.find_element_by_id("id_subject")).select_by_visible_text(course['category'])  # 选择主题
#     selenium.find_element_by_id("id_title").send_keys(course['title'])  # 输入文章标题
#     selenium.find_element_by_id("id_overview").send_keys(course['description'])  # 输入描述
#     selenium.find_element_by_class_name("default").click()  # 点击保存
#
#
# @then("页面中应存在名称为<标题>的链接")
# def check_course(course):
#     assert EC.presence_of_element_located(("link text", course['title']))
#
#
# @then("删除该课程")
# def delete_course(selenium, course):
#     selenium.find_element_by_link_text(course['title']).click()
#     selenium.find_element_by_class_name("deletelink").click()
#     selenium.find_element_by_css_selector("input[type='submit']").click()


@when("登录EneMicro")
def login(selenium, user):
    selenium.get(BaseUrl)
    time.sleep(5)
    selenium.find_element_by_id('username').send_keys(user['username'])
    selenium.find_element_by_id('password').send_keys(user['password'])
    selenium.find_element_by_id('loginButton').click()
    time.sleep(5)


@then('登录成功，进入账户概览页面')
def check_login():
    assert EC.presence_of_element_located(("link text", '账户概览'))
