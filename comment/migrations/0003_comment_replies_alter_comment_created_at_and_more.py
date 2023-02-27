# Generated by Django 4.1.6 on 2023-02-26 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0008_rename_createdat_group_created_at_and_more'),
        ('users', '0005_rename_createdat_user_created_at_and_more'),
        ('reply', '0001_initial'),
        ('comment', '0002_rename_createdat_comment_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='reply.reply'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='group.group'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user'),
        ),
    ]
