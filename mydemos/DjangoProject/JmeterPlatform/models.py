from django.db import models
from os import path


class Script(models.Model):
    s_author = models.CharField(max_length=16, verbose_name=u'脚本作者')
    s_file_name = models.CharField(max_length=100, verbose_name=u'脚本名称')
    s_file = models.CharField(max_length=100, verbose_name=u'脚本路径')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'script'
        ordering = ['-create_time']


class Data(models.Model):
    d_file_name = models.CharField(max_length=100)
    d_file = models.CharField(max_length=100)
    d_script = models.ForeignKey(Script, on_delete=models.CASCADE, related_name='d_script')

    class Meta:
        db_table = 'data'
