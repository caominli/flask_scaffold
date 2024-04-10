from flask import render_template, Blueprint,g
from flask_babel import _, refresh

lang = Blueprint('lang', __name__, template_folder='templates', url_prefix='/<lang_code>')
#指定一个蓝图模块，目录为lang,并指定这个蓝图组件默认模板目录为templates,url_prefix指定路由前缀变量

#根据路由前缀变量来识别语言，保存在g.lang_code全局变量中
@lang.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')


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

@lang.route('/2')
def cn():
    # g.lang_code = 'zh_hans'
    # refresh() #重新加载翻译
    return render_template('2.html', title=_('这是中文标题'))

