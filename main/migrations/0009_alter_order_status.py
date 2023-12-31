# Generated by Django 3.2.20 on 2023-08-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_order_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Success', 'Success')], default='Pending', max_length=10, verbose_name='Status'),
        ),
    ]
