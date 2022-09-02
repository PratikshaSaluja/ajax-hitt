# Generated by Django 3.1.12 on 2022-06-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomweb', '0010_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address_line1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address_line2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
    ]
