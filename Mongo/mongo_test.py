# coding:utf-8

import pymongo
import sys
from datetime import datetime

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "tacey_py"
MONGODB_VIDEO_COLLECTION = "video"
# collection = db[MONGODB_VIDEO_COLLECTION]


def conn():
    try:
        #连接数据库
        connection = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
        print "连接成功"
        #获得数据库连接句柄
        db = connection[MONGODB_DB]
        # assert db.collection == connection
        print "成功建立数据库柄"
        return db    
    except Exception as e:
        print "------"
        print str(e)
        print "-------"
        sys.stderr.write(str(e))
        sys.exit(1)

def insert(db,doc):

    #向users集合插入一条文档
    #若users集合不存在,会自动创建
    #w保证插入多个数据库才能
    try:
        db.users.insert(doc,w=1)#,safe=True)
        print "成功插入文档:%s" %doc
    except Exception as e:
        print e

def rake():
    user_doc = {
            "username":"Amber",
            "firstname":"Tian",
            "sourcename":"Doe",
            "dateofbirth":datetime(1993,12,8),
            "email":"285289578@qq.com",
            "score":0
    }
    db = conn()
    # insert(db,user_doc)
    user_doc = db.users.find_one({"username":"Amber"})
    if not user_doc:
        print "没有查到文档"
    print "-------------------------"
    #获取全部适合条件的全部信息
    user_doc = db.users.find({"username":"Amber"})
    for user in user_doc:
        print user.get("email")
        # print user["email"]
        print "+"*10

    #只获取email值
    user_doc = db.users.find({"username":"Amber"},{"email":1})
    for user in user_doc:
        print user
        print "-"*10
    #查看一个集合中有多少文档
    user_count = db.users.find().count()
    print user_count

    #以某个字段对查询结果进行排序
    user_doc = db.users.find({"username":"Amber"}).sort(("datebirth",pymongo.DESCENDING)).limit(10)
    for user in user_doc :
        print user
if __name__ == "__main__":
    rake()


