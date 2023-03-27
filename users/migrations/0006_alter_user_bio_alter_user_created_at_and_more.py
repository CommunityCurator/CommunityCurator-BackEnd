# Generated by Django 4.1.6 on 2023-02-27 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0009_alter_group_created_at_alter_group_users'),
        ('users', '0005_rename_createdat_user_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, to='group.group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]