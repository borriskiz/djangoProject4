import django_filters

from handmade import models

class HandmadeFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.HandmadeItem
        fields = ['name','price']