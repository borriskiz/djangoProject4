from django.db import models


class ItemType(models.Model):
    name = models.CharField(verbose_name="Type name", max_length=255)
    BOUGHT_CHOICES = [
        ("bought", "Bought"),
        ("not_bought", "Not Bought"),
    ]
    is_bought = models.CharField(
        verbose_name="Item Bought Status",
        max_length=10,
        choices=BOUGHT_CHOICES,
        default="not_bought",
    )


    class Meta:
        verbose_name = "Item Type"
        verbose_name_plural = "Item Types"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(verbose_name="Material name", max_length=255)
    dealer = models.ForeignKey(
        "Dealer", on_delete=models.SET_NULL, blank=True, null=True
    )
    price = models.IntegerField(verbose_name="Material price")
    color = models.CharField(verbose_name="Material color", max_length=255, blank=True)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"
        ordering = ["name", "-price"]

    def __str__(self):
        return f"{self.name} - {self.color}"


class Dealer(models.Model):
    name = models.CharField(verbose_name="Dealer name", max_length=255)
    contact_info = models.CharField(verbose_name="Dealer contact info", max_length=255)

    class Meta:
        verbose_name = "Dealer"
        verbose_name_plural = "Dealers"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(verbose_name="Market name", max_length=255, unique=True)
    location = models.CharField(verbose_name="Market location", max_length=255)
    contact_info = models.CharField(
        verbose_name="Market contact info", max_length=255, default="no info"
    )

    class Meta:
        verbose_name = "Market"
        verbose_name_plural = "Markets"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", unique=True)
    phone = models.CharField(verbose_name="Phone Number", max_length=20, blank=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def total_cost(self):

        total = 0
        for item in self.handmadeitem_set.all():
            total += item.price
        return total


class HandmadeItem(models.Model):
    name = models.CharField(verbose_name="Item name", max_length=255)

    date_receipt = models.DateField(verbose_name="Date of receipt", blank=True)
    item_type = models.ForeignKey(
        ItemType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Item type",
    )
    materials = models.ManyToManyField(
        Material,
        verbose_name="Item material",
    )
    market = models.ForeignKey(
        Market,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Item market",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        verbose_name="Item picture", upload_to="items/", blank=True, null=True
    )
    customers = models.ManyToManyField(
        Customer,
        related_name="handmade_items",
        verbose_name="Customers",
        blank=True,
    )

    class Meta:
        verbose_name = "Handmade Item"
        verbose_name_plural = "Handmade Items"
        ordering = ["-price"]

    def __str__(self):
        return f"{self.name} - {self.price}"


class Profile(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Customer Profile",
    )
    address = models.CharField(verbose_name="Address", max_length=255, blank=True)
    date_of_birth = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.customer.first_name}'s Profile"