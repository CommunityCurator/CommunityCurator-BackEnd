# Generated by Django 4.1.6 on 2023-02-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_bio_alter_user_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='Miami', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='Florida', max_length=50),
            preserve_default=False,
        ),
    ]
