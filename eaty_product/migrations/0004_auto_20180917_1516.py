# Generated by Django 2.0.7 on 2018-09-17 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eaty_product', '0003_auto_20180831_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='dislike',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='producttype',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
