# Generated by Django 3.1.2 on 2020-10-17 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-post_date', 'name']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-post_date']},
        ),
    ]