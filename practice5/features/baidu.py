#encoding=utf-8
# language: zh-CN
from lettuce import *
from selenium import webdriver
import time

@step(u'将搜索词设定为书的名字"(.*)"')
def have_the_searchWord(step, searchWord):
    world.searchWord = searchWord
    print world.searchWord

@step(u'打开百度网站')
def visit_baidu_website(step):
    world.driver = webdriver.Firefox(executable_path = "c:\\geckodriver")
    world.driver.get("http://www.baidu.com")

@step(u'在搜索输入框中输入搜索的关键词，并点击搜索按钮后')
def search_in_sogou_website(step):
    world.driver.find_element_by_id("kw").send_keys(world.searchWord)
    world.driver.find_element_by_id("su").click()
    time.sleep(3)

@step(u'在搜索结果中可以看到书的作者"(.*)"')
def check_result_in_sogou(step, searchResult):
    assert searchResult in world.driver.page_source, "got word:%s" %searchResult
    world.driver.quit()
