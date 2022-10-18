from django.db import models

from category.models import Category
from django.contrib.auth import get_user_model

from city.models import City

User = get_user_model()


# Create your models here.

class Hotel(models.Model):
    owner = models.ForeignKey(User, on_delete= models.RESTRICT,
                              related_name= 'products')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,null=True,   # КОГДА УДАЛИМ КАТЕГОРИЮ НЕ УДАЛЯЕТСЯ ПРОДУКТ
                                 related_name='products')               # ЗА МЕСТУ КАТЕГОРИИ СТОИТ null
    images = models.ImageField(upload_to ='images')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='products', null=True)
    class Meta:
        ordering = ['title']


    def __str__(self):
        return self.title