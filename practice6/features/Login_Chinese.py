#encoding=utf-8
# language: zh-CN
from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@step(u'启动一个浏览器')
def open_browser(step):
    try:
        # 创建Chrome浏览器的driver实例，并存于全局对象world中，
        # 供后续场景或步骤函数使用
        world.driver = webdriver.Firefox(executable_path="c:\\geckodriver")

    except Exception, e:
        raise e

@step(u'用户访问(.*)网址')
def visit_url(step, url):
    print url
    world.driver.get(url)

@step(u'用户输入输入用户名“(.*)”和密码“(.*)”')
def user_enters_UserName_and_Password(step, username, password):
    print username, password
    # 浏览器窗口最大化
    world.driver.maximize_window()
    time.sleep(3)
    # 切换进frame控件
    world.driver.switch_to.frame("x-URS-iframe")
    # 获取用户名输入框
    userName = world.driver.find_element_by_xpath('//input[@name="email"]')
    userName.clear()
    # 输入用户名
    userName.send_keys(username)
    # 获取密码输入框
    pwd = world.driver.find_element_by_xpath("//input[@name='password']")
    # 输入密码
    pwd.send_keys(password)
    # 发送一个回车键
    pwd.send_keys(Keys.RETURN)
    # 等待15秒，以便登录后成功进入登录后的页面
    time.sleep(15)

@step(u'页面会出现“(.*)”关键字')
def message_displayed_Login_Successfully(step, keywords):
    # print world.driver.page_source.encode('utf-8')
    # 断言登录成功后，页面是否出现预期的关键字
    world.driver.switch_to.default_content()#后添加
    assert keywords in world.driver.page_source
    # 断言成功后，打印登录成功信息
    print "Login Success"

@step(u'用户从页面单击退出链接')
def LogOut_from_the_Application(step):
    print "====",world.driver
    # time.sleep(5)
    world.driver.switch_to.default_content()#后添加
    # 点击退出按钮，退出登录
    world.driver.find_element_by_link_text(u"退出").click()
    time.sleep(8)

@step(u'页面显示“(.*)”关键内容')
def displayed_LogOut_Successfully(step, keywords):
    # 断言退出登录后，页面是否出现退出成功关键内容
    assert keywords in world.driver.page_source
    print u"Logout Success"
    # 退出浏览器
    world.driver.quit()
