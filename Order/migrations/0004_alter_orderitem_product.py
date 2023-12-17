# Generated by Django 4.2.6 on 2023-12-14 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_remove_product_order_item'),
        ('Order', '0003_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product'),
        ),
    ]
