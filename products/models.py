from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name=_('title'), max_length=50, unique=True)
    description = models.TextField(verbose_name=_('description'), blank=True, )
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='categories/')
    is_enabled = models.BooleanField(verbose_name=_('is enabled'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50, unique=True)
    description = models.TextField(verbose_name=_('description'), blank=True, )
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='products/')
    is_enabled = models.BooleanField(verbose_name=_('is enabled'), default=True)
    categories = models.ManyToManyField(Category, verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)
    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey(Product,verbose_name=_('product'), on_delete=models.CASCADE)
    file = models.FileField(verbose_name=_('file'), upload_to='files/%Y/%m/%d/')
    title = models.CharField(verbose_name=_('title'), max_length=50, unique=True)
    is_enabled = models.BooleanField(verbose_name=_('is enabled'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)
    def __str__(self):
        return self.title
