# Generated by Django 4.2.5 on 2023-09-29 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('user_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Account.user')),
                ('courier_name', models.CharField(max_length=50)),
                ('fee', models.FloatField()),
            ],
            bases=('Account.user',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Account.user')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
            ],
            bases=('Account.user',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Account.user')),
                ('company_name', models.CharField(max_length=50)),
            ],
            bases=('Account.user',),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.customer')),
            ],
        ),
    ]
