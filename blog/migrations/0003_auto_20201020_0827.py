# Generated by Django 3.1.2 on 2020-10-20 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20201017_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-post_date', 'id']},
        ),
        migrations.AlterModelOptions(
            name='blogger',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-post_date', 'id']},
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='last_name',
        ),
        migrations.AddField(
            model_name='blogger',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
