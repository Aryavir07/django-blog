# Generated by Django 3.1.3 on 2020-12-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click on post name to read complete post!', max_length=70),
        ),
    ]