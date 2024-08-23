#这是一个视图蓝图模块，不需要引入app，将直接在app/__init__.py中引入
from flask import Blueprint, render_template
# from .models import User, DB
from .task import huey,sendcode

view = Blueprint('view', __name__)

@view.route('/')
def index():
    # # 使用连接池，创建一个用户
    # with DB.connection_context():
    #     user = User(email='test@example.com', password='123456')
    #     user.save()
    #添加一个任务
    huey.enqueue(sendcode.s(priority=10))
    return render_template('index.html',text='欢迎来到首页')