# Generated by Django 3.1.2 on 2020-10-17 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('text', models.TextField(help_text='Enter a text of blog')),
            ],
            options={
                'ordering': ['post_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=1000)),
                ('blog', models.ManyToManyField(to='blog.Blog')),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogger')),
            ],
            options={
                'ordering': ['post_date'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blogger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogger'),
        ),
    ]
