from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    use = models.TextField(blank=True)
    diametr = models.CharField(blank=True,max_length=100)
    len = models.CharField(blank=True,max_length=100)
    color = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    cat_id = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

