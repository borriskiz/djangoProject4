"""
URL configuration for django2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from handmade.views import (
    CustomerAPI,
    HandmadeItemListView,
    HandmadeItemDetailView,
    HandmadeItemCreateView,
    HandmadeItemUpdateView,
    HandmadeItemDeleteView, HandmadeItemAPI, ItemTypeAPI, MarketAPI, DealerAPI, MaterialAPI, ProfileAPI,

)

router = DefaultRouter()
router.register('item_types', ItemTypeAPI, basename='item_types')
router.register('customers', CustomerAPI, basename='customers')
router.register('handmade_items', HandmadeItemAPI, basename='handmade_items')
router.register('markets', MarketAPI, basename='markets')
router.register('dealers', DealerAPI, basename='dealers')
router.register('materials', MaterialAPI, basename='materials')
router.register('profiles', ProfileAPI, basename='profiles')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
                  # path('', start_page, name='start_page'),  # Добавляем путь для стартовой страницы
                  path('handmade-items/', HandmadeItemListView.as_view(), name='handmade_item_list'),
                  path('handmade-items/<int:pk>/', HandmadeItemDetailView.as_view(), name='handmade_item_detail'),
                  path('handmade-items/create/', HandmadeItemCreateView.as_view(), name='handmade_item_create'),
                  path('handmade-items/update/<int:pk>/', HandmadeItemUpdateView.as_view(),
                       name='handmade_item_update'),
                  path('handmade-items/delete/<int:pk>/', HandmadeItemDeleteView.as_view(),
                       name='handmade_item_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
