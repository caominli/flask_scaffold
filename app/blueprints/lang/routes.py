from flask import render_template, Blueprint
from app import app

lang = Blueprint('lang', __name__, template_folder='templates') #指定一个蓝图模块，目录为lang,并指定这个蓝图组件默认模板目录为templates

#指定这个蓝图组件的路由
@lang.route('/')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)