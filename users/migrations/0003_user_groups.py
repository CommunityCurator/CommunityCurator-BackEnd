# Generated by Django 4.1.5 on 2023-02-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_group_users'),
        ('users', '0002_rename_created_at_user_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='group.group'),
        ),
    ]