# Generated by Django 3.1.3 on 2020-12-16 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
    ]