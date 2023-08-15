# Generated by Django 3.2.20 on 2023-08-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_clientprofile_shipping_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='shipping_location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Shipping Location'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='shipping_street',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Shipping Street'),
        ),
    ]