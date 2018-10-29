#encoding=utf-8
from lettuce import *

@step('I have the following students in my database:')
def students_in_database(step):
    if step.hashes:
        # ������ڲ��������ݣ��������������
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
    # ��ͨ��������ʽƥ�䲽�������һ����ĸ��
    # ������ȫ�ֱ���startAlpha��
    world.startAlpha = startAlpha
    print "no data exist:",step.hashes

@step('I see those billed students:')
def get_starting_with_G_student(step):
    # �����������ݱ��е�����
    for i in step.hashes:
        # ����ѧ���������Ƿ���world.startAlpha������ȡ�ĵ���ĸ��ͷ
        assert i["name"].startswith(world.startAlpha)

@step("those that weren't:")
def result(step):
    for j in step.hashes:
        # ����ѧ�����ֲ���world.startAlpha������ȡ�ĵ���ĸ��ͷ
        # ����ѧ�����ֲ���world.startAlpha������ȡ�ĵ���ĸ��ͷ
        assert world.startAlpha not in j["name"][0]
