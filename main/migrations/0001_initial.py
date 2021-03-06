# Generated by Django 3.0.5 on 2020-04-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('district', models.CharField(blank=True, max_length=120, null=True, verbose_name='Район, округ')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('images_path', models.CharField(blank=True, max_length=1024, verbose_name='Путь сохраненных фото')),
                ('url', models.CharField(blank=True, max_length=1024, verbose_name='Ссылка объявления')),
                ('published_date', models.DateField(verbose_name='Дата публикации на сайте')),
                ('write_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('source', models.CharField(max_length=120, verbose_name='Ресурс объявлсения')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
