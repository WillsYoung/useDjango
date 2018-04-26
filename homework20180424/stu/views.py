
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse

from stu.models import Student, Class, StudentInfo


def show_student(request):
    return HttpResponse('This is the student table!')


def show_class(request):
    return HttpResponse('This is the class table!')


def add_stu(request):
    if request.method == 'GET':
        return render(request, 'add_student.html')
    if request.method == 'POST':
        r = request.POST
        stu_name = r['name']
        stu_sex = 1 if r['sex'] == '男' else 0
        stu_birth = r['birth']
        stu_tel = r['tel']
        stu_class = r['class']
        c_id = Class.objects.get(c_name=stu_class).id

        Student.objects.create(
            stu_name=stu_name,
            stu_sex=stu_sex,
            stu_birth=stu_birth,
            stu_tel=stu_tel,
            stu_class=stu_class,
            g_id=c_id
        )
        s_id = Student.objects.get(stu_name=stu_name).id
        # 跳转到另一个html页面并且传入多个参数
        # return HttpResponseRedirect(
        #     reverse('/school/stuinfo/', kwargs={'s_id': s_id})
        # )
        return HttpResponseRedirect('/school/stuinfo/' + '?sinfo_id=' + str(s_id))


def stuinfo(request):
    if request.method == 'GET':
        s_id = request.GET.get('sinfo_id')
        return render(request, 'add_stuinfo.html', {'s_id': s_id})
    if request.method == 'POST':
        r = request.POST
        addr = r['addr']
        s_id = request.GET.get('sinfo_id')
        StudentInfo.objects.create(
            stu_addr=addr,
            sinfo_id=int(s_id)
        )
        return HttpResponseRedirect('/school/all_info' + '?id=' + s_id)


def allinfo(request):
    stu_id = request.GET.get('id')
    stu = Student.objects.get(id=stu_id)
    info = StudentInfo.objects.get(sinfo_id=stu_id)
    return render(request, 'allinfo.html', {'stu': stu, 'info': info})


def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')

    if request.method == 'POST':
        r = request.POST
        c_name = r['name']
        c_nums = r['numbers']
        c_intro = r['intro']

        Class.objects.create(
            c_name=c_name,
            c_stu_nums=c_nums,
            c_intro=c_intro
        )
        return HttpResponse('添加班级信息成功')


def show(request):
    return render(request, 'index.html')


def student_table1(request):
    stu_class = request.GET.get('')
    if stu_class:
        stus = Student.objects.all().filter(stu_class=stu_class)
    else:
        stus = Student.objects.all()
    return render(request, 'student.html', {'stus': stus})


def student_table(request, c_id):
    g_id = c_id
    if int(g_id):
        # 演示500错误页面 stus = Student.objects.all().get(g_id=300)
        stus = Student.objects.all().filter(g_id=c_id)
    else:
        stus = Student.objects.all()
    return render(request, 'student.html', {'stus': stus})


def student_table2(request, c_id):
    # 写业务逻辑然后业务中转到另一个方法继续处理
    return HttpResponseRedirect(
        reverse('s:re', kwargs={'g_id': c_id})
    )


def redirect_stu(request, c_id):
    stus = Student.objects.filter(g_id=c_id)
    return render(request, 'student.html', {'stus': stus})


def selstu(request, m, n, p):
    return HttpResponse('获取url传递多个参数的方法')


def actstu(request, year, day, month):
    return HttpResponse('获取url中指定的参数')


def class_table(request):
    c = Class.objects.all()
    return render(request, 'class.html', {'c': c})


def allstu(request):
    c = Class.objects.all().filter(c_name='js')
    s = Student.objects.all().filter(stu_class='js')
    return render(request, 'js.html', {'c': c, 'stus': s})


def page_not_found(request):
    return render(request, '404.html')


def server_error(request):
    return render(request, '500.html')


def delstu(request):
    stu_id = request.GET.get('stu_id')

    s = Student.objects.get(id=stu_id)

    Student.objects.filter(id=stu_id).delete()
    return HttpResponseRedirect('/school/student.html/' + str(s.g_id))


def upstu(request):
    stu_id = request.GET.get('stu_id')
    stu = Student.objects.get(id=stu_id)
    stu.stu_name = '修改'
    stu.save()

    s = Student.objects.get(id=stu_id)
    # 将所要跳转到网页重定向
    return HttpResponseRedirect('/school/student.html/' + str(s.g_id))

