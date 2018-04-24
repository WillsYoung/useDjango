python下面有很多Web框架，django是最好的几种之一
Web框架基本都是符合MVC实现模式
M：model模型--V:view视图--C:controller控制器
它的核心思想就是解耦合，即一个模块干好一件事情就好了
优点：降低各个模块的耦合性，方便变更，更容易重构代码，最大程度复用代码
Django对mvc模式的具体实现是MVT: model view template
下面是创建django项目的基本步骤
1.  下载安装虚拟环境模块
    pip install virtualenv
2.  创建一个虚拟环境
    virtualenv --no-site-packages +文件夹
3.  进入虚拟环境安装django，并且检查是否安装成功
    pip install django==1.11
    在pyhton交互式环境下
    import django
    django.get_version()
    如返回django的版本就表示ok
4.  创建第一个django项目
    django-admin startproject day2
5.  启动django项目
    python manage.py runserver 8888（8888表示端口，不写默认8000）
6.  创建一个app
    python manage.py startapp app1
7.  app1文件夹下面文件的主要内容及其含义
    __init__.py:初始化，配置pymysql的地方
    admin.py : 管理后台注册模型的地方
    apps.py: setting.朋友里面注册app时候回用到一般不推荐
    models.py ： 定义数据库模型，写模型的地方
    test.py ： 写测试方法，脚本的地方
    views.py ： 写业务处理的逻辑的地方
    setting.py： 配置信息所在的位置，例如调用访问哪里的数据库
    urls.py ： URL路由
    wsgi.py ： 网关
8.  模型
    在models.py 中定义class模型的名称
    继承models.Model
    db_table：定义数据库中表的名称
9.  迁移数据库
    python manage.py makemigrations
    python manage.py migrate
10. 保存数据
    stu = Student（）
    stu.sex = 1
    stu.name = '张山'
11. 创建超级管理员账号密码
    python manage.py createsuperuser
12. 进行orm 对象关系映射
13. 模型字段的含义
    CharField（5）： 字符串长度5
    BooleanField()： 布尔型数 0/1
    DateField()   :  年 月 日
    DateTimeField（）： 年月日时分秒
    auto_now_add :   参数 -- 在创建时生成永远不会改变，比如某个人的生日
    auto_now     :   参数 -- 创建时生成，但是每次登录就用当前时间覆盖，比如某人的登录记录
    AutoField     ： 自动增长，一般用于id主键上
    models.DecimalField(max_digits=3,decimal_digits=1)
    参数max_digits=3表示数字最大位数为3，decimal_digits=1表示小数点后1wei
    这个数最大为99.9

    TextFIE的： 存储文本信息，图片等超长字符串
    IntegerField：整数
    models.FloatField:浮点数

    models.FileField():文件信息上传字段
    models.ImageField(upload_to='xx/xx/aa.png')： 图片上传并给以路径

14. 模型参数（约束条件）
    default：默认
    null：设置是否为空，针对数据库中某个字段是否可以为空
    blank：设置是否为空，针对网页表单提交某字段可否为空
