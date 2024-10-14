from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from handmade.models import HandmadeItem

class HandmadeItemListView(ListView):
    model = HandmadeItem
    template_name = 'handmade/handmade_item_list.html'
    context_object_name = 'items'

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
    success_url = reverse_lazy('handmade_item_list')

class HandmadeItemDeleteView(DeleteView):
    model = HandmadeItem
    template_name = 'handmade/handmade_item_confirm_delete.html'
    success_url = reverse_lazy('handmade_item_list')