# Generated by Django 4.0 on 2021-12-27 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('Blog', '0003_module'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Module',
            new_name='PostModule',
        ),
        migrations.CreateModel(
            name='DisadvantagesModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.postmodule')),
            ],
        ),
        migrations.CreateModel(
            name='AdvantagesModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.postmodule')),
            ],
        ),
    ]
