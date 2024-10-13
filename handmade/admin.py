from django.contrib import admin
from handmade import models

# Register your models here.


admin.site.register(models.ItemType)


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = {"name"}


admin.site.register(models.Material)


class MaterialAdmin(admin.ModelAdmin):
    list_display = {"name"}


admin.site.register(models.Dealer)


class DealerAdmin(admin.ModelAdmin):
    list_display = {"name"}


admin.site.register(models.Market)


class MarketAdmin(admin.ModelAdmin):
    list_display = {"name"}


admin.site.register(models.Customer)


class CustomerAdmin(admin.ModelAdmin):
    list_display = {"first_name", "last_name"}


admin.site.register(models.HandmadeItem)


class HandmadeItemAdmin(admin.ModelAdmin):
    list_display = {"name"}


admin.site.register(models.Profile)


class ProfileAdmin(admin.ModelAdmin):
    list_display = {"address"}
