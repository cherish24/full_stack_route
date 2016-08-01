#coding:utf-8
import codecs
# with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:

import os

#系统类型
print os.name

#系统具体名称
print os.uname()

#系统变量
# print os.environ

#获取系统变量的值
print os.getenv("PATH")
#当前目录的绝对地址
print os.path.abspath('.')

#组合路径
os.path.join()
#拆分路径
os.path.split()
#获得文件扩展名
os.path.splitext()

# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')



#部分功能不是系统调用，os中没有提供
import shutil



#序列化
#cPicle/pickle
#dict

# pickle.dump()
pickle.loads()
#JSON(反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。)
#类实例转换为字典print(json.dumps(s, default=lambda obj: obj.__dict__))