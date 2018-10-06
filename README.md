# 如何新建一个简单的 Django rest framework 工程

## 环境
1. Python 3.6
2. Django 2.0.7

## 步骤
1. 新建一个简单的 django 项目(此处省略)
2. 下载 django rest framework

```
pip install djangorestframework
```
3.配置setting.py

```
INSTALLED_APPS = [
    ...
    "rest_framework",
    ...
]
```
4.在 view.py 中使用django rest framework( 以下简称 DRF)

```
from rest_framework.views import APIView
from rest_framework.response import Response

class home(APIView):
    
    def get(self,request):
        # get 请求
        return Response("我是 DRF GET")

    def post(self, request):
        # post 请求
        return Response("我是 DRF POST")
```
5.配置 urls.py

```
...
from app01 import views
urlpatterns = [
    ...
    path('home/', views.home.as_view()),
    ...
]
```







