#coding:utf-8

from flask import Flask , url_for , request , json

app = Flask(__name__)

@app.route('/')
def api_root():
    return "api root"

@app.route("/articles")
def api_articles():
    return "List of"+url_for("api_articles")

@app.route("/articles/<int:article_id>")
def api_article(article_id):
    return "正在阅读{}".format(article_id)

@app.route("/hello")
def hello():
    if 'name' in request.args:
        return "Hello " + request.args['name']
    else:
        return "Hello Tacey"

@app.route("/echo", methods=['GET','POST','DELETE','PATCH','PUT'])
def api_echo():
    if request.method == "GET":
        return "GET"
    elif request.method == "POST":
        return "POST"
    elif request.method == "DELETE":
        return "DELETE"
    elif request.method == "PATCH":
        return "PATCH"
    elif request.method == "PUT":
        return "PUT"


@app.route("/messages",methods=["POST"])
def api_messages():
    # 可以通过request.files获取上传的文件 curl可以用-F选项模拟上传
    if request.headers["Content-Type"] == "text/plain":
        return "文本消息："+request.data
    elif request.headers["Content-Type"] == "application/json":
        return "JSON消息："+json.dumps(request.json)
    elif request.headers["Content-Type"] == "application/octet-stream":
        f = open("./binary" , 'wb')
        f.write(request.data)
        f.close()
        return "二进制文件写入成功"
    else:
        return "415 不支持的媒体类型",415

from flask import Response

@app.route("/hellos" , methods = ["GET"])
def api_hello():
    data = {
        "hello" : "world",
        "number" : 3
    }
    js = json.dumps(data)
    resp = Response(js,status=200,mimetype="application/json")
    resp.headers["link"] = "http://www.baidu.com"
    resp.headers["Server"] = "Tacey's Tiny Server'"
    return resp

    


if __name__ == "__main__":
    app.run(debug=True)



