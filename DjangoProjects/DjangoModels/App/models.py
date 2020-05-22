from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=16)


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class Script(models.Model):
    s_author = models.CharField(max_length=16, verbose_name=u'脚本作者')
    s_file_name = models.CharField(max_length=100, verbose_name=u'脚本名称')
    s_file = models.FileField(upload_to='upload/JmeterScript')
    create_time = models.DateTimeField(auto_now_add=True)


class Data(models.Model):
    d_file_name = models.CharField(max_length=100)
    d_file = models.FileField(upload_to='upload/JmeterData')
    d_script = models.ForeignKey(Script, on_delete=models.CASCADE)


