#encoding=utf-8
from lettuce import *

@step('I have the following students in my database:')
def students_in_database(step):
    if step.hashes:
        # 如果存在步骤表格数据，则继续后续步骤
        print type(step.hashes)
        assert step.hashes == [
            {
                'name': 'Anton',
                'monthly_due': '$ 500',
                'billed': 'no'
            },
            {
                'name': 'Jack',
                'monthly_due': '$ 400',
                'billed': 'no'
            },
            {
                'name': 'Gabriel',
                'monthly_due': '$ 300',
                'billed': 'no'
            },
            {
                'name': 'Gloria',
                'monthly_due': '$ 442.65',
                'billed': 'no'
            },
            {
                'name': 'Ken',
                'monthly_due': '$ 907.86',
                'billed': 'no'
            },
            {
                'name': 'Leonard',
                'monthly_due': '$ 742.84',
                'billed': 'no'
            },
        ]

@step('I bill names starting with "(.*)"')
def match_starting(step, startAlpha):
    # 将通过正则表达式匹配步骤中最后一个字母，
    # 并存于全局变量startAlpha中
    world.startAlpha = startAlpha
    print "no data exist:",step.hashes

@step('I see those billed students:')
def get_starting_with_G_student(step):
    # 遍历步骤数据表中的数据
    for i in step.hashes:
        # 断言学生的名字是否以world.startAlpha变量存取的的字母开头
        assert i["name"].startswith(world.startAlpha)

@step("those that weren't:")
def result(step):
    for j in step.hashes:
        # 断言学生名字不以world.startAlpha变量存取的的字母开头
        # 断言学生名字不以world.startAlpha变量存取的的字母开头
        assert world.startAlpha not in j["name"][0]
