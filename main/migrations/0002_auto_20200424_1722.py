# Generated by Django 3.0.5 on 2020-04-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='published_date',
            field=models.DateTimeField(verbose_name='Дата публикации на сайте'),
        ),
    ]
