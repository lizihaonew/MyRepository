# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Data(models.Model):
    d_file_name = models.CharField(max_length=100)
    d_file = models.CharField(max_length=100)
    d_script = models.ForeignKey('Script', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Script(models.Model):
    s_author = models.CharField(max_length=16)
    s_file_name = models.CharField(max_length=100)
    s_file = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    deleted = models.IntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'script'


class Task(models.Model):
    task_name = models.CharField(max_length=32)
    start_time = models.CharField(max_length=16)
    end_time = models.CharField(max_length=16)
    thread_count = models.IntegerField()
    loop_time = models.IntegerField()
    ramp_up = models.IntegerField()
    status = models.IntegerField()
    operator = models.CharField(max_length=16)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'task'
