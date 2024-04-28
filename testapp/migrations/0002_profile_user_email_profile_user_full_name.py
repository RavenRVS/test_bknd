# Generated by Django 5.0.3 on 2024-03-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user_full_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]