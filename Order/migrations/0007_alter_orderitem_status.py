# Generated by Django 4.2.6 on 2023-12-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]