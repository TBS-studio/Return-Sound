from从烧瓶进口*import *
from来自泡菜进口*import *
应用程序=烧瓶（__名称__）Flask(__name__)

@@app.route('/',methods=["get","post"])('/',methods=["get","post"])
defdef index(): # 将应用程序的代码放在这里index():  # put application's code here
    返回 render_template("index.html",error="")return render_template("index.html",error="")
    user=request.values.get("用户")values.get("user")
    pwd=request.values.get("pwd")values.get("pwd")
    如果用户不在用户中：if user not in users:
        return render_template("index.html",error="用户名不存在")return render_template("index.html",error="用户名不存在")
    elif 用户[用户] != pwd:elif users[user] != pwd:
        return render_template("index.html",error="密码不正确")return render_template("index.html",error="密码不正确")
    别的：else:
        会话[“用户”]=用户["user"]=user
        session.permanent=Truepermanent=True
        返回 render_template("index.html")return render_template("index.html")
    
try尝试：
    以 open("users.pickle","rb") 作为 f：with open("users.pickle","rb") as f:
        用户=负载（f）load(f)
except除了：
    用户={}{}
    

    
app.route("/登录",methods=["get","post"])route("/Login",methods=["get","post"])
defdef 登录():Login():
    user=request.values.get("用户")values.get("user")
    pwd=request.values.get("pwd")values.get("pwd")
    如果用户不在用户中：if user not in users:
        return render_template("index.html",error="用户名不存在")return render_template("index.html",error="用户名不存在")
    elif 用户[用户] != pwd:elif users[user] != pwd:
        return render_template("index.html",error="密码不正确")return  render_template  (  "index.html" ,error= "密码不正确"  )
    另外：
        会话[ “用户” ] = 用户
        session.永久=真
        返回渲染模板（“index.html”）html”）
    
    
应用程序跑步（）
