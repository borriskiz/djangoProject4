# Generated by Django 5.1.2 on 2024-10-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handmade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='items',
            field=models.ManyToManyField(to='handmade.handmadeitem', verbose_name='Items to purchase'),
        ),
    ]