# Generated by Django 3.0.6 on 2020-05-27 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_author', models.CharField(max_length=16, verbose_name='脚本作者')),
                ('s_file_name', models.CharField(max_length=100, verbose_name='脚本名称')),
                ('s_file', models.CharField(max_length=100, verbose_name='脚本路径')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'script',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=32, verbose_name='任务名称')),
                ('start_time', models.CharField(max_length=16, verbose_name='运行开始时间')),
                ('end_time', models.CharField(max_length=16, verbose_name='运行结束时间')),
                ('thread_count', models.IntegerField(verbose_name='线程数')),
                ('loop_time', models.IntegerField(verbose_name='循环次数')),
                ('ramp_up', models.IntegerField(verbose_name='启动时间')),
                ('status', models.IntegerField(verbose_name='运行状态')),
                ('operator', models.CharField(max_length=16, verbose_name='操作人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'task',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_file_name', models.CharField(max_length=100)),
                ('d_file', models.CharField(max_length=100)),
                ('d_script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='d_script', to='JmeterPlatform.Script')),
            ],
            options={
                'db_table': 'data',
            },
        ),
    ]
