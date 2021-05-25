#Feature: educa在线课程网站需求
#  需求描述: 提供后台添加课程及课程内容, 前台学生浏览课程, 加入课程后可查看课程详情
#
#  Scenario: 通过educa后台添加课程
#    Given 用户:hanzhichao, 密码:hanzhichao123
#    And 分类:接口测试,标题:Python接口测试教程,描述:作者,临渊
#    When 登录educa后台
#    And 点击:Courses模块->点击新增按钮
#    And 作者选择当前<用户>,选择<分类>,输入<标题>,<描述>,点击保存
#    Then 页面中应存在名称为<标题>的链接
#    And 删除该课程

Feature: EneMicro登录
  需求描述: 用户使用账号密码登录成功，并进入产品

  Scenario: 用户使用账号密码登录成功
    Given 用户:zhangbin, 密码:zb123456
    When 登录EneMicro
    Then 登录成功，进入账户概览页面
