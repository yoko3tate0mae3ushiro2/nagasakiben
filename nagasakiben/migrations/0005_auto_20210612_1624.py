# Generated by Django 2.2.24 on 2021-06-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagasakiben', '0004_auto_20210612_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='written_by',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='記事タイトル'),
        ),
    ]