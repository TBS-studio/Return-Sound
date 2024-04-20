from flask import *
from pickle import *
app = Flask(__name__)

@app.route('/',methods=["get","post"])
def index():  # put application's code here
    return render_template("index.html",error="")
    user=request.values.get("user")
    pwd=request.values.get("pwd")
    if user not in users:
        return render_template("index.html",error="用户名不存在")
    elif users[user] != pwd:
        return render_template("index.html",error="密码不正确")
    else:
        session["user"]=user
        session.permanent=True
        return render_template("index.html")
    
try: 
    with open("users.pickle","rb") as f:
        users = load(f)
except:
    users={}
    

    
app.route("/Login",methods=["get","post"])
def Login():
    user=request.values.get("user")
    pwd=request.values.get("pwd")
    if user not in users:
        return render_template("index.html",error="用户名不存在")
    elif users[user] != pwd:
        return render_template("index.html",error="密码不正确")
    else:
        session["user"]=user
        session.permanent=True
        return render_template("index.html")
    
    
app.run()
