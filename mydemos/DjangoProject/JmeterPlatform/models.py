from django.db import models
from os import path


class Script(models.Model):
    s_author = models.CharField(max_length=16, verbose_name=u'脚本作者')
    s_file_name = models.CharField(max_length=100, verbose_name=u'脚本名称')
    s_file = models.CharField(max_length=100, verbose_name=u'脚本路径')
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

