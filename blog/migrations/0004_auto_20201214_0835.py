# Generated by Django 3.1.3 on 2020-12-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201214_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='ML', max_length=255),
        ),
    ]
