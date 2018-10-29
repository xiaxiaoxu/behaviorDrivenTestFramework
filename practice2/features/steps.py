#encoding=utf-8
from lettuce import world, steps

def factorial(number):
  number = int(number)
  if (number == 0) or (number == 1):
    return 1
  else:
      return reduce(lambda x, y: x * y, range(1, number + 1))

@steps
class FactorialSteps(object):
    """Methods in exclude or starting with _ will not be considered as step"""

    exclude = ['set_number', 'get_number']

    def __init__(self, environs):
        # 初始全局变量
        self.environs = environs

    def set_number(self, value):
        # 设置全局变量中的number变量的值
        self.environs.number = int(value)

    def get_number(self):
        # 从全局变量中取出number的值
        return self.environs.number

    def _assert_number_is(self, expected, msg="Got %d"):
        number = self.get_number()
        # 断言
        assert number == expected, msg % number

    def have_the_number(self, step, number):
        '''I have the number (\d+)'''
        # 上面的三引号引起的代码必须写，并且必须是三引号引起
        # 表示从场景步骤中获取需要的数据
        # 并将获得数据存到环境变量number中
        self.set_number(number)

    def i_compute_its_factorial(self, step):
        """When I compute its factorial"""
        number = self.get_number()
        # 调用factorial方法进行阶乘结算，
        # 并将结算结果存于全局变量中的number中
        self.set_number(factorial(number))

    def check_number(self, step, expected):
        '''I see the number (\d+)'''
        # 上面的三引号引起的代码必须写，并且必须是三引号引起
        # 表示从场景步骤中获取需要的数据以便断言测试结果
        self._assert_number_is(int(expected))

FactorialSteps(world)
