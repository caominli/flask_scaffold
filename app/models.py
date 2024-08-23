from peewee import PrimaryKeyField, CharField,DateTimeField
from playhouse.pool import PooledPostgresqlDatabase # 引入Postgresql连接池
from playhouse.flask_utils import FlaskDB # 引入flask-peewee
from config import DataConfig #配置
from datetime import datetime 

# 配置连接池
try:
    database = PooledPostgresqlDatabase(
        database=DataConfig.name,
        user=DataConfig.user,
        password=DataConfig.password,
        host=DataConfig.host,
        port=DataConfig.port,
        max_connections=10,  # 设置最大连接数为10
        stale_timeout=5000  # 超时的连接被自动回收
    )
except Exception as e:
    print("程序停止,数据库连接失败:", e)
    raise SystemExit(e)  # 暂停程序

# 将peewee集成到flask中
peeweeDB = FlaskDB(database=database)


# 定义模型
class User(peeweeDB.Model):
    id = PrimaryKeyField()
    email = CharField(max_length=80, unique=True)
    password = CharField(max_length=160)
    created_at = DateTimeField(default=datetime.now)  # 自动写入时间


# 获取数据库实例
DB = peeweeDB.database

