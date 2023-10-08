from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class MenuModel(MPTTModel):
    """Древовидное меню"""
    name = models.CharField('Название', max_length=150, help_text='Максимум 100 символов')
    named_url = models.SlugField('URL', max_length=150, unique=True)
    parent = TreeForeignKey('self', verbose_name='Выберете поле', help_text='Выберете пункт', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']