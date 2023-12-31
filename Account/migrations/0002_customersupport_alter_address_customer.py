# Generated by Django 4.2.5 on 2023-10-07 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSupport',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Account.user')),
                ('support_name', models.CharField(max_length=50)),
            ],
            bases=('Account.user',),
        ),
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Account.customer'),
        ),
    ]
