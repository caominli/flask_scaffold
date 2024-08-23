# flask手脚架说明

```
项目目录
 ┣ app                  #应用目录
 ┃ ┣ templates          #模板文件
 ┃ ┃ ┣ base.html        #基础模板  
 ┃ ┃ ┗ index.html       #首页模板
 ┃ ┣ static             #静态文件
 ┃ ┣ common             #封装组件
 ┃ ┃ ┣ __init__.py      #(空)
 ┃ ┃ ┣ sendemail.py     #发送电子邮件
 ┃ ┣ __init__.py        #初始化app实列
 ┃ ┣ models.py          #peewee模型
 ┃ ┣ views.py           #视图路由
 ┃ ┣ api.py             #api路由
 ┃ ┗ task.py            #任务列队[可选调用]
 ┣ run.py               #调试运行文件
 ┣ config.py            #配置文件
 ┣ requirements.txt     #依赖文件
 ┗ README.md
```

### task任务列队启动消费者


