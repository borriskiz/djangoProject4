import django_filters
from django.db.models import Q
from handmade import models
from handmade.models import ItemType, Market


class HandmadeFilterSet(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(lookup_expr='icontains', field_name='price', label='Цена от и до')
    original = django_filters.BooleanFilter(method='filter_original', field_name='original',
                                            label='Собственного производства')
    term = django_filters.CharFilter(method='filter_term', label='Поиск')
    item_type = django_filters.ModelChoiceFilter(queryset=ItemType.objects.all(), field_name='item_type',
                                                 label='Тип предмета')
    market = django_filters.ModelChoiceFilter(queryset=Market.objects.all(), field_name='market',
                                              label='Рынок')

    class Meta:
        model = models.HandmadeItem
        fields = ['term', 'item_type', 'price_range', 'original']

    def filter_original(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(item_type__is_bought='not_bought')
        return queryset.filter(item_type__is_bought="bought")

    def filter_term(self, queryset,name, value):
        criteria = Q()
        for term in value.split():
            criteria = Q(name__icontains=term) | Q(item_type__name__icontains=term)
        return queryset.filter(criteria).distinct()
