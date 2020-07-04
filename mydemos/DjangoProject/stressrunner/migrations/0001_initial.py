# Generated by Django 2.1.4 on 2020-07-04 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnvGroup',
            fields=[
                ('env_id', models.AutoField(primary_key=True, serialize=False, verbose_name='环境组ID')),
                ('env_name', models.CharField(max_length=50, verbose_name='环境组名称')),
                ('owner', models.CharField(max_length=20, verbose_name='提交人')),
                ('master_node', models.CharField(max_length=30, verbose_name='master节点')),
                ('slave_node', models.CharField(blank=True, max_length=256, null=True, verbose_name='slave节点')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_name', models.CharField(default='root', max_length=20, verbose_name='机器用户名')),
                ('user_password', models.CharField(max_length=100, verbose_name='机器密码')),
                ('test_time', models.DateTimeField(blank=True, null=True, verbose_name='测试时间')),
                ('is_used', models.CharField(choices=[('0', '空闲'), ('1', '占用')], default=0, max_length=1, verbose_name='是否被占用')),
                ('set_status', models.CharField(choices=[('0', '待部署'), ('1', '部署成功'), ('2', '部署失败'), ('3', '部署中')], default='0', max_length=1, verbose_name='部署状态')),
                ('test_status', models.CharField(choices=[('0', '待测试'), ('1', '测试成功'), ('2', '测试失败')], default='0', max_length=1, verbose_name='环境组状态')),
            ],
            options={
                'verbose_name': '环境组维护',
                'verbose_name_plural': '环境组维护',
                'db_table': 'env_groups',
            },
        ),
        migrations.CreateModel(
            name='InterfaceName',
            fields=[
                ('interface_id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('interface_name', models.CharField(max_length=50, verbose_name='接口名称')),
                ('interface_percent', models.IntegerField(blank=True, null=True, verbose_name='接口占比')),
            ],
            options={
                'verbose_name': '接口表',
                'verbose_name_plural': '接口表',
                'db_table': 'interface_name',
            },
        ),
        migrations.CreateModel(
            name='ProjectRepo',
            fields=[
                ('project_id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='项目id')),
                ('project_name', models.CharField(max_length=20, verbose_name='库名称')),
                ('project_addr', models.CharField(max_length=256, verbose_name='git库地址')),
                ('project_author', models.CharField(max_length=15, verbose_name='脚本库作者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '脚本库',
                'verbose_name_plural': '脚本库',
                'db_table': 'project_repo',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ProjectScenarios',
            fields=[
                ('proscen_id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='编号')),
                ('proscen_name', models.CharField(max_length=128, verbose_name='脚本文件')),
                ('proscen_path', models.CharField(max_length=256, verbose_name='脚本路径')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stressrunner.ProjectRepo')),
            ],
            options={
                'verbose_name': 'git库和场景对应关系',
                'verbose_name_plural': 'git库和场景对应关系',
                'db_table': 'repo_scenarios',
            },
        ),
        migrations.CreateModel(
            name='Scenarios',
            fields=[
                ('scenario_id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('scenario_file', models.CharField(max_length=128, verbose_name='脚本文件')),
                ('scenario_path', models.CharField(max_length=256, verbose_name='场景路径')),
                ('thread_num', models.IntegerField(default=0, verbose_name='并发数')),
                ('rampup_time', models.IntegerField(verbose_name='启动时间')),
                ('run_status', models.CharField(choices=[('0', '待运行'), ('1', '运行中'), ('2', '已运行'), ('3', '运行失败')], default='0', max_length=1, verbose_name='运行状态')),
                ('report_url', models.URLField(blank=True, null=True, verbose_name='报告地址')),
                ('env_name', models.CharField(max_length=50, verbose_name='环境组名称')),
                ('master_node', models.CharField(max_length=30, verbose_name='master节点')),
                ('slave_node', models.CharField(blank=True, max_length=256, null=True, verbose_name='slave节点')),
                ('env', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stressrunner.EnvGroup', verbose_name='环境')),
            ],
            options={
                'verbose_name': '场景表',
                'verbose_name_plural': '场景表',
                'db_table': 'scenarios',
            },
        ),
        migrations.CreateModel(
            name='StressTask',
            fields=[
                ('task_id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='任务id')),
                ('task_name', models.CharField(max_length=150, verbose_name='任务名称')),
                ('task_content', models.CharField(blank=True, max_length=128, null=True, verbose_name='任务描述')),
                ('task_owner', models.CharField(max_length=20, verbose_name='创建人')),
                ('git_name', models.CharField(max_length=50, verbose_name='脚本库名称')),
                ('git_addr', models.CharField(max_length=256, verbose_name='脚本库地址')),
                ('duration', models.IntegerField(verbose_name='运行时间')),
                ('next_run_time', models.DateTimeField(verbose_name='任务执行时间')),
                ('status', models.CharField(choices=[('0', '待运行'), ('1', '运行中'), ('2', '已运行'), ('3', '运行失败')], default='0', max_length=20, verbose_name='任务状态')),
                ('hosts_path', models.CharField(max_length=100, verbose_name='host文件')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_monitored', models.IntegerField(default=0, verbose_name='是否被调度器监控')),
            ],
            options={
                'verbose_name': '压测任务',
                'verbose_name_plural': '压测任务',
                'db_table': 'stress_tasks',
                'ordering': ['-create_at'],
            },
        ),
        migrations.AddField(
            model_name='scenarios',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stressrunner.StressTask', verbose_name='任务'),
        ),
        migrations.AddField(
            model_name='interfacename',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stressrunner.Scenarios', verbose_name='场景'),
        ),
    ]
