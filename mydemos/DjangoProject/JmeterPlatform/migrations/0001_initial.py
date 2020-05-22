# Generated by Django 3.0.6 on 2020-05-21 13:21

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
                ('u_name', models.CharField(max_length=16)),
                ('u_file_name', models.CharField(max_length=100)),
                ('u_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_file_name', models.CharField(max_length=100)),
                ('d_file', models.FileField(upload_to='')),
                ('d_script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JmeterPlatform.Script')),
            ],
        ),
    ]
