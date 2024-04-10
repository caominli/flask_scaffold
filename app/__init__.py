from flask import Flask
app = Flask(__name__) #在__init__中指定的直接在目录中访问对象

from app.blueprints.lang import lang #导入一个蓝图组件

app.register_blueprint(lang) #注册蓝图