# Generated by Django 3.2.5 on 2021-08-14 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
    ]
