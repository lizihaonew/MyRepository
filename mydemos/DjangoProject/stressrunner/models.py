from django.db import models

# Create your models here.


class StressTask(models.Model):
    """ 压测任务 """

    task_id = models.AutoField(primary_key=True, db_index=True, verbose_name="任务id")
    task_name = models.CharField(verbose_name="任务名称", max_length=30)
    task_content = models.CharField(verbose_name="任务描述", max_length=50, null=True, blank=True)
    task_owner = models.CharField(verbose_name="创建人", max_length=20)
    git_name = models.CharField(verbose_name="脚本库名称", max_length=20)
    git_addr = models.CharField(verbose_name="脚本库地址", max_length=128)
    duration = models.IntegerField(verbose_name="运行时间")
    next_run_time = models.DateTimeField(verbose_name="任务执行时间")
    status = models.CharField(verbose_name="任务状态", max_length=1, default='0', choices=((u'0', "待运行"),
                                                                           (u'1', "运行中"),
                                                                           (u'2', "已运行"),
                                                                           (u'3', "运行失败"),
                                                                           (u'4', u"已试压,待运行"),
                                                                           (u'5', u"试压失败,待运行"),
                                                                           (u'6', "已停止"),
                                                                           (u'7', "停止失败")))
    # host文件地址
    hosts_path = models.CharField(verbose_name="host文件", max_length=128)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新时间", null=True, blank=True, auto_now=True)
    # delat = models.DateTimeField(verbose_name="删除时间", null=True, blank=True)
    is_monitored = models.IntegerField(verbose_name="是否被调度器监控", default=0)
    ext_param = models.CharField(verbose_name="扩展字段", max_length=50, null=True, blank=True, default=0)

    class Meta:
        ordering = ['-create_at']
        db_table = 'stress_tasks'
        verbose_name = "压测任务"
        verbose_name_plural = "压测任务"

    def __str__(self):
        return self.task_name


class ProjectRepo(models.Model):

    """ 脚本库 """

    project_id = models.AutoField(primary_key=True, db_index=True, verbose_name="项目id")
    project_name = models.CharField(max_length=20, verbose_name="库名称")
    project_addr = models.CharField(max_length=128, verbose_name="git库地址")
    project_author = models.CharField(max_length=15, verbose_name="脚本库作者")
    git_username = models.CharField(max_length=20, verbose_name="git用户名")
    git_password = models.CharField(max_length=100, verbose_name="git密码")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", null=True, blank=True, auto_now=True)
    ext_param = models.CharField(verbose_name="扩展字段", max_length=50, null=True, blank=True, default=0)

    class Meta:
        ordering = ['-create_time']
        db_table = 'project_repo'
        verbose_name = "脚本库"
        verbose_name_plural = "脚本库"

    def __str__(self):
        return self.project_name


class EnvGroup(models.Model):
    """ 环境组 """

    env_id = models.AutoField(primary_key=True, verbose_name="环境组ID")
    env_name = models.CharField(max_length=50, verbose_name="环境组名称")
    owner = models.CharField(max_length=20, verbose_name="提交人")
    master_node = models.CharField(max_length=30, verbose_name="master节点")
    slave_node = models.CharField(max_length=512, blank=True, null=True, verbose_name="slave节点")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    user_name = models.CharField(max_length=20, verbose_name="机器用户名", default="root")
    user_password = models.CharField(max_length=20, verbose_name="机器密码")
    test_time = models.DateTimeField(null=True, blank=True, verbose_name="测试时间")
    is_used = models.CharField(max_length=1, default=0, choices=((u'0', u"空闲"),
                                                                 (u'1', u"占用")), verbose_name="是否被占用")
    set_status = models.CharField(max_length=1, verbose_name="部署状态", default='0', choices=((u'0', u"待部署"),
                                                                                         (u'1', u"部署成功"),
                                                                                         (u'2', u"部署失败"),
                                                                                         (u'3', u"部署中")))
    test_status = models.CharField(choices=(
        (u'0', u"待测试"),
        (u'1', u"测试成功"),
        (u'2', u"测试失败")
    ), max_length=1, default='0', verbose_name="环境组状态")
    ext_param = models.CharField(verbose_name="扩展字段", max_length=50, null=True, blank=True, default=0)

    class Meta:
        db_table = 'env_groups'
        verbose_name = "环境组维护"
        verbose_name_plural = "环境组维护"

    def __str__(self):
        return self.env_name


class Scenarios(models.Model):

    """ 场景表 """
    scenario_id = models.AutoField(primary_key=True, db_index=True)
    scenario_file = models.CharField(max_length=30, verbose_name="脚本文件")
    is_throughput = models.IntegerField(verbose_name="脚本是否为吞吐量模式", default=1)
    scenario_path = models.CharField(max_length=128, verbose_name="场景路径")
    thread_num = models.IntegerField(verbose_name="并发数", default=0)
    rampup_time = models.IntegerField(verbose_name="启动时间")
    run_status = models.CharField(choices=((u'0', u"待运行"),
                                           (u'1', u"运行中"),
                                           (u'2', u"已运行"),
                                           (u'3', u"运行失败"),
                                           (u'4', u"已试压,待运行"),
                                           (u'5', u"试压失败,待运行"),
                                           (u'6', "已停止"),
                                           (u'7', "停止失败")),
                                  max_length=1, default='0', verbose_name="运行状态")
    report_url = models.URLField(verbose_name="报告地址", blank=True, null=True)
    env_name = models.CharField(max_length=30, verbose_name="环境组名称")
    master_node = models.CharField(max_length=30, verbose_name="master节点")
    slave_node = models.CharField(max_length=512, blank=True, null=True, verbose_name="slave节点")
    job_id = models.CharField(max_length=194, blank=True, null=True, verbose_name="job id")
    fail_reason = models.CharField(max_length=150, blank=True, null=True, verbose_name="运行失败原因")

    task = models.ForeignKey(
        StressTask,
        on_delete=models.CASCADE,
        verbose_name="任务")

    env = models.ForeignKey(
        EnvGroup,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="环境")

    # env_id = ""
    ext_param = models.CharField(verbose_name="扩展字段", max_length=50, null=True, blank=True, default=0)

    class Meta:
        db_table = 'scenarios'
        verbose_name = "场景表"
        verbose_name_plural = "场景表"

    def __str__(self):
        return self.scenario_file


class InterfaceName(models.Model):
    """ 接口占比表 """

    interface_id = models.AutoField(primary_key=True, db_index=True)
    interface_name = models.CharField(max_length=40, verbose_name="接口名称")
    interface_percent = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="接口占比", blank=True, null=True)
    scenario = models.ForeignKey(
        Scenarios,
        on_delete=models.CASCADE,
        verbose_name="场景")

    class Meta:
        db_table = 'interface_name'
        verbose_name = "接口表"
        verbose_name_plural = "接口表"

    def __str__(self):
        return self.interface_name
