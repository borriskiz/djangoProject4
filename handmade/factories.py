import factory

from handmade.models import HandmadeItem, ItemType, Market, Material


class ItemTypeFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = ItemType


class MaterialFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    price = factory.Faker('random_int', min=1, max=1000)
    color = factory.Faker('color_name')

    class Meta:
        model = Material


class MarketFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('company')
    location = factory.Faker('address')
    contact_info = factory.Faker('phone_number')

    class Meta:
        model = Market


class HandmadeItemFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('sentence')
    date_receipt = factory.Faker('date')
    item_type = factory.SubFactory(ItemTypeFactory)
    market = factory.SubFactory(MarketFactory)
    price = factory.Faker('random_int', min=1, max=1000)
    image = factory.django.ImageField(color='blue')

    materials = factory.RelatedFactoryList(
        MaterialFactory,
        factory_related_name='handmadeitem',
        size=3
    )

    class Meta:
        model = HandmadeItem