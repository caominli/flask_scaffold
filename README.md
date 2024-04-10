# flask手脚架说明

目录结构
```
project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── api.py
│   ├── static/
│   │   └── ...
│   │   └── img/
│   ├── templates/
│   │   └── base.html
│   │   └── index.html
│   │   └── ...
│   └── blueprints/
│       └── auth/
│       │   ├── __init__.py
│       │   ├── views.py
│       │   ├── forms.py
│       └── blog/
│           ├── __init__.py
│           ├── views.py
│           ├── forms.py
├── config.py
├── requirements.txt
└── run.py
```