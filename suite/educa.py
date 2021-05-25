# file_name: test_educa.py
from pytest_bdd import scenario
from step.scenario_steps import *  # 导入场景解释/支持步骤


@scenario("../feature/educa.feature", "用户使用账号密码登录成功")
def test_login():  # 测试educa需求文件中名为"通过educa后台添加课程"的场景
    pass   # 可以不写内容, pass即可
