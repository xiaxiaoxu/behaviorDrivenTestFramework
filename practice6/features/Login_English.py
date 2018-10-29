#encoding=utf-8
from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@step('Launch a browser')
def open_browser(step):
    try:
        world.driver =  webdriver.Firefox(executable_path="c:\\geckodriver")

    except Exception, e:
        raise e

@step('User visit to (.*) Page')
def visit_url(step, url):
    world.driver.get(url)

@step('User enters UserName"(.*)" and Password"(.*)"')
def user_enters_UserName_and_Password(step, username, password):
    world.driver.maximize_window()
    time.sleep(3)
    world.driver.switch_to.frame("x-URS-iframe")
    userName = world.driver.find_element_by_xpath('//input[@name="email"]')
    userName.clear()
    userName.send_keys(username)
    pwd = world.driver.find_element_by_xpath("//input[@name='password']")
    pwd.send_keys(password)
    pwd.send_keys(Keys.RETURN)
    time.sleep(15)

@step('Message displayed Login Successfully')
def message_displayed_Login_Successfully(step):
    # print world.driver.page_source.encode('utf-8')
    world.driver.switch_to.default_content()#后添加
    assert u"未读邮件" in world.driver.page_source
    print "Login Success"

@step('User LogOut from the Application')
def LogOut_from_the_Application(step):
    print "====",world.driver
    # time.sleep(15)
    world.driver.switch_to.default_content()#后添加
    world.driver.find_element_by_link_text(u"退出").click()
    time.sleep(4)

@step('Message displayed LogOut Successfully')
def displayed_LogOut_Successfully(step):
    assert u"您已成功退出网易邮箱" in world.driver.page_source
    print u"Logout Success"
    world.driver.quit()
