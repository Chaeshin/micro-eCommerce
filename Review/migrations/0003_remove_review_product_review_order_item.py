# Generated by Django 4.2.6 on 2023-11-04 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_orderitem_product'),
        ('Review', '0002_reviewvote_review_review_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.AddField(
            model_name='review',
            name='order_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Order.orderitem'),
        ),
    ]
