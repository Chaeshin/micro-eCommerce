# Generated by Django 4.2.6 on 2023-10-10 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_alter_courier_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='type',
            new_name='user_type',
        ),
    ]