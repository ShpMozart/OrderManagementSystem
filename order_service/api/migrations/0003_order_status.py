# Generated by Django 5.1.2 on 2024-10-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_inventory_remove_order_name_remove_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
