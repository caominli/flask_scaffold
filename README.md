# flask手脚架说明



### task任务列队启动消费者
在项目目录下，启动2个消费者线程
`huey_consumer.py app.task.huey -w 2`
`python venv\Scripts\huey_consumer.py app.task.huey -w 2`
如果需要使用redis，pip install redis

### 如果不需要huey任务列队模块
- 删除requirements.txt中的huey
- 删除app/__init__.py中的huey代码
- 删除app/tesk.py


