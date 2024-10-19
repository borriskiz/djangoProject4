import django_filters

from handmade import models


class HandmadeFilterSet(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(lookup_expr='icontains', field_name='price', label='Цена от и до')
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='name', label='Название предмета')
    original = django_filters.BooleanFilter(method='filter_original', field_name='originality',
                                            label='Собственного произовдства')

    class Meta:
        model = models.HandmadeItem
        fields = ['name', 'price_range', 'item_type']

    def filter_original(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(item_type__is_bought='bought')
        return queryset.filter(item_type__is_bought="not_bought")
