from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from rest_framework import viewsets

from handmade import serializers
from handmade.filters import HandmadeFilterSet
from handmade.models import HandmadeItem, Customer, ItemType, Market, Dealer, Profile, Material


def start_page(request):
    return redirect('handmade_item_list')


class CustomerAPI(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class HandmadeItemAPI(viewsets.ModelViewSet):
    queryset = HandmadeItem.objects.all()
    serializer_class = serializers.HandmadeItemSerializer


class ItemTypeAPI(viewsets.ModelViewSet):
    queryset = ItemType.objects.all()
    serializer_class = serializers.ItemTypeSerializer


class MarketAPI(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = serializers.MarketSerializer


class DealerAPI(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = serializers.DealerSerializer


class ProfileAPI(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class MaterialAPI(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = serializers.MaterialSerializer


class HandmadeItemListView(FilterView):
    model = HandmadeItem
    template_name = 'handmade/handmade_item_list.html'
    context_object_name = 'items'
    filterset_class = HandmadeFilterSet


class HandmadeItemDetailView(DetailView):
    model = HandmadeItem
    template_name = 'handmade/handmade_item_detail.html'
    context_object_name = 'item'


class HandmadeItemCreateView(CreateView):
    model = HandmadeItem
    template_name = 'handmade/handmade_item_form.html'
    fields = ['name', 'date_receipt', 'item_type', 'materials', 'market', 'price', 'image']

    def get_success_url(self):
        return reverse_lazy('handmade_item_detail', kwargs={'pk': self.object.pk})


class HandmadeItemUpdateView(UpdateView):
    model = HandmadeItem
    template_name = 'handmade/handmade_item_form.html'
    fields = ['name', 'date_receipt', 'item_type', 'materials', 'market', 'price', 'image']
    success_url = reverse_lazy('handmade_item_list')


class HandmadeItemDeleteView(DeleteView):
    model = HandmadeItem
    template_name = 'handmade/handmade_item_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('handmade_item_list')
