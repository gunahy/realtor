from django.db import models

# Create your models here.


class Announce(models.Model):
    """
    address
    district
    options
    price
    images
    url
    source
    phonenumber
    """
    title = models.CharField(max_length=255, blank=False, verbose_name='Наименование')
    address = models.CharField(max_length=255, blank=False, verbose_name='Адрес')
    district = models.CharField(max_length=120, blank=True, null=True, verbose_name='Район, округ')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    images_path = models.CharField(max_length=1024, blank=True, verbose_name='Путь сохраненных фото')
    url = models.CharField(max_length=1024, blank=True, verbose_name='Ссылка объявления')
    #published_date = models.DateTimeField(verbose_name='Дата публикации на сайте')
    write_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    source = models.CharField(max_length=120, blank=False, verbose_name='Ресурс объявлсения')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Options(models.Model):
    """
    type
    kind
    rooms
    floor
    square
    buildings_material
    """
    pass