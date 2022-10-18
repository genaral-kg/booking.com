from django.db.models import Avg
from rest_framework import serializers

from category.models import Category
from .models import Hotel

class HotelListSerializer(serializers.ModelSerializer):                ####ЗДЕСЬ МЫ УКАЖЕМ ЧТО НАМ ВОЗВРАШАТЬ НА GET ЗАПРОС
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Hotel
        fields = ('owner','title','price','images','city')                   ###  ТОЧНЕЕ ЗДЕСЬ МЫ УКАЖЕМ

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']

        return repr


class HotelDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    category = serializers.PrimaryKeyRelatedField(required=True,queryset= Category.objects.all())    #БЕЗ КАТЕГОРИИ НЕ МОЖЕМ ТЕПЕРЬ СОЗДАТЬ ПРОДУКТ

    class Meta:
        model = Hotel
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['rating_count'] = instance.reviews.count()
        return repr

