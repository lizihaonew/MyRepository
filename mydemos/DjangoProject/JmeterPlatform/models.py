from django.db import models
from os import path


class Script(models.Model):
    s_author = models.CharField(max_length=16, verbose_name=u'脚本作者')
    s_file_name = models.CharField(max_length=100, verbose_name=u'脚本名称')
    s_file = models.CharField(max_length=100, verbose_name=u'脚本路径', blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(blank=True)

    class Meta:
        db_table = 'script'
        ordering = ['-create_time']


class Data(models.Model):
    d_file_name = models.CharField(max_length=100)
    d_file = models.CharField(max_length=100)
    d_script = models.ForeignKey(Script, on_delete=models.CASCADE, related_name='d_script')

    class Meta:
        db_table = 'data'


class Task(models.Model):
    task_name = models.CharField(max_length=32, verbose_name=u'任务名称')
    start_time = models.CharField(max_length=16, verbose_name=u'运行开始时间')
    end_time = models.CharField(max_length=16, verbose_name=u'运行结束时间')
    thread_count = models.IntegerField(verbose_name=u'线程数')
    loop_time = models.IntegerField(verbose_name=u'循环次数')
    ramp_up = models.IntegerField(verbose_name=u'启动时间')
    status = models.IntegerField(verbose_name=u'运行状态0')
    operator = models.CharField(max_length=16, verbose_name=u'操作人')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        db_table = 'task'
        ordering = ['-create_time']


class Person(models.Model):
    p_id = models.AutoField(primary_key=True, verbose_name='person_id')
    name = models.CharField(max_length=16, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')

    class Meta:
        db_table = 'person'


class PersonInfo(models.Model):
    info_id = models.AutoField(primary_key=True, verbose_name='info_id')
    sex = models.BooleanField(default=0)
    birth = models.DateField()
    tel = models.CharField(max_length=11)
    person = models.OneToOneField(Person, on_delete=models.SET_NULL, null=True, related_name='info')

    class Meta:
        db_table = 'person_info'


class Author(models.Model):
    author_id = models.AutoField(primary_key=True, verbose_name='author_id')
    name = models.CharField(max_length=16, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')

    class Meta:
        db_table = 'author'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True, verbose_name='book_id')
    book_name = models.CharField(max_length=16, verbose_name='书名')
    page = models.IntegerField(verbose_name='页数')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='book')

    class Meta:
        db_table = 'book'


class Colors(models.Model):
    colors = models.CharField(max_length=10, verbose_name='颜色')

    class Meta:
        db_table = 'color'

    def __str__(self):
        return self.colors


class Child(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    favor = models.ManyToManyField(Colors)

    class Meta:
        db_table = 'child'

    def __str__(self):
        return self.name
