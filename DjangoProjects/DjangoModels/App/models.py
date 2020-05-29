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


class UserType(models.Model):
    nid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=16)

    class Meta:
        db_table = 'user_type'


class UserInfo(models.Model):
    # CharFiled类型不能为空，最好要指定一个长度
    user = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    pwd = models.CharField(max_length=32)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name='type_user')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        db_table = 'user_info'








