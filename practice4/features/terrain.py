﻿#encoding=utf-8
from lettuce import *
import logging

# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level = logging.INFO,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # 打印日志的时间
    datefmt = '%a, %Y-%m-%d %H:%M:%S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    filename = 'd:/BddDataDriveRreport.log',
    # 打开日志文件的方式
    filemode = 'w'
)
# 在所有场景执行前执行
@before.all
def say_hello():
    logging.info("Lettuce will start to run tests right now...")
    print "Lettuce will start to run tests right now..."

# 在每个secnario开始执行前执行
@before.each_scenario
def setup_some_scenario(scenario):
    # 每个Scenario开始前，打印场景的名字
    print 'Begin to execute scenario name:' + scenario.name
    # 将开始执行的场景信息打印到日志
    logging.info('Begin to execute scenario name:' + scenario.name)

# 每个step开始前执行
@before.each_step
def setup_some_step(step):
    run = "running step %r, defined at %s" % (
        step.sentence, # 执行的步骤
        step.defined_at.file # 步骤定义在哪个文件
    )
    # 将每个场景的每一步信息打印到日志
    logging.info(run)

# 每个step执行后执行
@after.each_step
def teardown_some_step(step):
    if not step.hashes:
       print "no tables in the step"   #会被打印9次，因为我们仅仅设定了场景的table，而不是给每个步骤设定table
                                       #注意每个step可以有自己的table,等价于把table的数据作为一个字典传入到程序中使用。
       logging.info("no tables in the step")

# 在每个secnario执行结束执行
@after.each_scenario
def teardown_some_scenario(scenario):
    print  'finished, scenario name:' + scenario.name
    logging.info('finished, scenario name:' + scenario.name)

# 在所有场景开始执行后执行
@after.all #默认获取执行结果的对象作为total参数
def say_goodbye(total):
    result = "Congratulations, %d of %d scenarios passed!" % (
        total.scenarios_ran,  #一共多少场景运行了
        total.scenarios_passed #一共多少场景运行成功了
    )
    print result
    logging.info(result)
    # 将测试结果写入日志文件
    logging.info("Goodbye!")
    print "------ Goodbye! ------"
