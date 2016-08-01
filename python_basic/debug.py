#coding:utf-8

#错误处理
#try-except-finally机制
import pdb

s = '0'
n = int(s)
print 10 / n

pdb.set_trace()#运行到此，自动暂停
import logging

logging.basicConfig(level = logging.INFO)
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'

#调试
# print
# assert 断言（python -O关闭断言）
# 