# Generated by Django 4.1.7 on 2023-03-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, help_text='helper', max_length=5000, null=True),
        ),
    ]
