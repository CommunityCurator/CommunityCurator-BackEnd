# Generated by Django 4.1.6 on 2023-04-05 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='groups',
        ),
    ]
