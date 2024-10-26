from rest_framework import serializers
from handmade import models

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemType
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Market
        fields = '__all__'


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dealer
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    dealer = DealerSerializer()

    class Meta:
        model = models.Material
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = models.Profile
        fields = '__all__'


class HandmadeItemSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True)
    customers = CustomerSerializer(many=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = models.HandmadeItem
        fields = ('id', 'name', 'date_receipt', 'item_type', 'materials', 'market', 'price', 'image', 'customers')

    def get_price(self, obj):
        if obj.item_type and obj.item_type.is_bought == "bought":
            return obj.price
        else:
            return obj.price + 20
