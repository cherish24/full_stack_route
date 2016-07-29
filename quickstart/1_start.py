# coding:utf-8

from flask import Flask , request ,url_for , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "这里是主页"

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html" , name=name)

@app.route("/user/<username>")
def show_user_profile(username):
    return "User:{}".format(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post:{}".format(post_id)

@app.route('/projects/')
def projects():
    return "This is project page"

@app.route("/about/")
def about():
    return "This is about page"

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        return "do the login"
    else:
        return "show the login form"





# url_for('static' , filename="sss")


if __name__ == "__main__":
    app.run(debug=True ,  host='0.0.0.0')