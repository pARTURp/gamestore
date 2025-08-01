# Generated by Django 5.1.6 on 2025-07-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_name_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('address', models.CharField(max_length=100, verbose_name='адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('products', models.TextField(verbose_name='Состав заказа')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итого')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачен')),
            ],
        ),
    ]
