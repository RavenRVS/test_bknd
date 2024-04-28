# Generated by Django 5.0.3 on 2024-03-17 17:43

import django.db.models.deletion
import testapp.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_profile_user_email_profile_user_full_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=testapp.models.user_directory_path)),
                ('name', models.CharField(max_length=250)),
                ('comment', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_download', models.DateTimeField(blank=True, null=True)),
                ('size', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'файл пользователя',
                'verbose_name_plural': 'Файлы пользователей',
            },
        ),
    ]