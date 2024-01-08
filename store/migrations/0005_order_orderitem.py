# Generated by Django 5.0.1 on 2024-01-08 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'PENDING'), ('CF', 'CONFIRMED'), ('C', 'CANCELLED'), ('CP', 'COMPLETED')], default='P', max_length=2)),
                ('payment_status', models.BooleanField(default=False)),
                ('shipping_address', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('P', 'PENDING'), ('CF', 'CONFIRMED'), ('C', 'CANCELLED'), ('CP', 'COMPLETED')], default='P', max_length=2)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
