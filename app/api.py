#一个蓝图模块，定义api，这里的所有路由前面都会加上/api
from flask import Blueprint,request,jsonify
api = Blueprint('api', __name__,url_prefix='/api')


#定义一个api
@api.route('/hello')
def index():
    return '{"msg":"Hello,API"}',200


#定义一个post方法,接收josn，并返回接收到的json
@api.route('/post',methods=['POST'])
def post():
    #取得请求的数据
    data = request.get_json()
    # 检查是否成功获取数据
    if data is None:
        return jsonify({'err': '获取数据失败'}), 400
    
    return jsonify({'msg': data}),200