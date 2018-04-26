from django.db import models

# Create your models here.


class Class(models.Model):
    c_name = models.CharField(max_length=6)
    c_stu_nums = models.IntegerField()
    c_intro = models.CharField(max_length=20)

    class Meta:
        db_table = 'class'


class Student(models.Model):
    stu_name = models.CharField(max_length=6)
    stu_sex = models.BooleanField(default=0)
    stu_birth = models.DateField()
    stu_tel = models.CharField(max_length=11)
    stu_class = models.CharField(max_length=12, default=0)
    g = models.ForeignKey(Class, null=True)

    class Meta:
        db_table = 'student'


class StudentInfo(models.Model):
    stu_addr = models.CharField(max_length=15)

    sinfo = models.OneToOneField(Student, null=True)

    class Meta:
        db_table = 'stu_info'


