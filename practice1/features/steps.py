#encoding=utf-8
from lettuce import *

# 用于计算整数的阶乘函数
def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, number + 1))

@step('I have the number (\d+)')
def have_the_number(step, number):
    # 将通过正则表达式匹配的数字存于全局变量world中
    world.number = int(number)

@step('I compute its factorial')
def compute_its_factorial(step):
    # 从全局变量world中取出匹配的数字，
    # 计算其阶乘，并将结果再存回world中
    world.number = factorial(world.number)

@step('I see the number (\d+)')
def check_number(step, expected):
    # 通过正则匹配到预期数字
    expected = int(expected)
    # 断言计算阶乘结果是否等于预期
    assert world.number == expected, "Got %d" %world.number
