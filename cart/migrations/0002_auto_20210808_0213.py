# Generated by Django 3.2.5 on 2021-08-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Shop',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
