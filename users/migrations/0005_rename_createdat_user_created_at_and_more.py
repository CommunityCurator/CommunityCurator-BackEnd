# Generated by Django 4.1.6 on 2023-02-23 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_createdat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='user_name',
        ),
    ]
