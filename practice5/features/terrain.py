#encoding=utf-8
from lettuce import *
from log import *

# 在所有场景执行前执行
@before.all
def say_hello():
    logging.info(u"开始执行行为数据驱动测试...")

# 在每个secnario开始执行前执行
@before.each_scenario
def setup_some_scenario(scenario):
    # 将开始执行的场景信息打印到日志
    logging.info(u'开始执行场景“%s”' %scenario.name)

# 每个step开始前执行
@before.each_step
def setup_some_step(step):
    world.stepName = step.sentence
    run = u"执行步骤“%s”, 定义在“%s”文件" % (
        step.sentence, # 执行的步骤
        step.defined_at.file # 步骤定义在哪个文件
    )
    # 将每个场景的每一步信息打印到日志
    logging.info(run)

# 每个step执行后执行
@after.each_step
def teardown_some_step(step):
    logging.info(u"步骤“%s”执行结束" % world.stepName)

# 在每个secnario执行结束执行
@after.each_scenario
def teardown_some_scenario(scenario):
    logging.info(u'场景“%s”执行结束' %scenario.name)

# 在所有场景开始执行后执行
@after.all #默认获取执行结果的对象作为total参数
def say_goodbye(total):
    result = u"恭喜，%d个场景运行，%d个场景运行成功" % (
        total.scenarios_ran,  #一共多少场景运行了
        total.scenarios_passed #一共多少场景运行成功了
    )
    logging.info(result)
    # 将测试结果写入日志文件
    logging.info(u"本次行为数据驱动执行结束")
