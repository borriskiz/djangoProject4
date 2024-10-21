import factory

from models import HandmadeItem, Customer, ItemType,Market,Material

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
    materials = factory.List([factory.SubFactory(MaterialFactory) for _ in range(3)])  # Создает 3 материала
    market = factory.SubFactory(MarketFactory)
    price = factory.Faker('random_int', min=1, max=1000)
    image = factory.django.ImageField(color='blue')  # Генерирует заглушку изображения

    class Meta:
        model = HandmadeItem

class CustomerFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone = factory.Faker('phone_number')
    items = factory.List([factory.SubFactory(HandmadeItemFactory) for _ in range(2)])  # Создает 2 HandmadeItem

    class Meta:
        model = Customer