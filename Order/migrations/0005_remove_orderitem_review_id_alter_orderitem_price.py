# Generated by Django 4.2.6 on 2023-12-16 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_alter_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='review_id',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(editable=False),
        ),
    ]
