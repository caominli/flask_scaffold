from flask import Flask,request,g
from flask_babel import Babel
from config import Config #导入项目根目录的config
from accept_language import parse_accept_language

app = Flask(__name__) #在__init__中指定的直接在目录中访问对象
app.config.from_object(Config) #使用配置文件

from app.blueprints.lang import lang #导入一个蓝图组件
app.register_blueprint(lang) #注册蓝图

#定义一个语言选择函数
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code

babel = Babel(app,locale_selector=get_locale)


