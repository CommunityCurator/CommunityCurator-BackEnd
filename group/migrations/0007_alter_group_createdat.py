# Generated by Django 4.1.6 on 2023-02-22 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_group_createdat_group_image_group_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='createdAt',
            field=models.DateTimeField(),
        ),
    ]
