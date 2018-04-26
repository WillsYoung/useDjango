"""homework20180424 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 这个scholl路径是我自己的app stu的相关事件处理的路径，即在url里面匹配到scholl即转到stuapp下面处理相应的请求
    url(r'school', include('stu.urls', namespace='s'))
]


from stu.views import page_not_found, server_error

# handler用来处理网页异常的反馈
handler404 = page_not_found
handler500 = server_error
