# Generated by Django 4.1.5 on 2023-02-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_created_at_user_createdat'),
        ('group', '0004_rename_category_group_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to='users.user'),
        ),
    ]
