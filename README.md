# useDjango
how to install environmnet of Django

for windows：
1. open cmd window
2. 首先下载虚拟环境模块 
   pip install virtualenv
3. 然后是创建一个虚拟环境
   virtualenv --no-site-packages +虚拟环境所在文件名 （默认只是安装了python3.6）
4. 然后进入虚拟环境，在虚拟环境下安装Django
   pip install django==1.11 （安装django1.11版本）
5. 查看有没有安装ok，可以进入python交互环境，然后
   import django
   django.get_version()
   如果安装成功，函数会返回安装的版本

for Linux：
1. linux版本是centos 7.6.4版本，安装了python3
2. 创建虚拟环境,选择一个保存虚拟环境的文件夹，并且进入
   python3 -m venv . 创建虚拟环境
   source bin/activate 进入虚拟环境
   deactivate        安全退出虚拟环境
3. 安装
