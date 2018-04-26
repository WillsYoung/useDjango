from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'student/', views.show_student),
    url(r'class/', views.show_class),
    url(r'add_stu/', views.add_stu),
    url(r'add_c/', views.add_class),
    url(r'show/$', views.show),
    url(r'studs', views.student_table1),
    url(r'student.html/(\d+)/', views.student_table, name='s'),
    url(r'class.html', views.class_table),
    url(r'js.html', views.allstu),
    url(r'redirectStu/(?P<g_id>\d+)', views.redirect_stu, name='re'),
    url(r'allstu/(\d+)/(\d+)/(\d+)/', views.selstu),
    url(r'actstu/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)',
        views.actstu),
    url(r'delstu', views.delstu),
    url(r'upstu', views.upstu),
    url(r'stuinfo', views.stuinfo),
    url(r'all_info', views.allinfo)
    ]