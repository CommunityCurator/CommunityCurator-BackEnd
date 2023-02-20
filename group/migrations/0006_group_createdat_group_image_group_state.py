# Generated by Django 4.1.6 on 2023-02-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_group_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='createdAt',
            field=models.DateField(default='2022-12-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='group',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]