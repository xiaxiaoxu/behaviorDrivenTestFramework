#encoding=utf-8
from lettuce import *

# 在所有场景执行前执行
@before.all
def say_hello():
    print u"开始执行行为数据驱动测试..."

# 在每个secnario开始执行前执行
@before.each_scenario
def setup_some_scenario(scenario):
    print u'开始执行场景“%s”' %scenario.name

# 在每个secnario执行结束后执行
@after.each_scenario
def teardown_some_scenario(scenario):
    print u'场景“%s”执行结束' %scenario.name

# 在所有场景执行结束后执行
@after.all #默认获取执行结果的对象作为total参数
def say_goodbye(total):
    result = u"恭喜，%d个场景被运行，%d个场景运行成功" % (
        total.scenarios_ran,  #一共多少场景运行了
        total.scenarios_passed #一共多少场景运行成功了
    )
    print result
