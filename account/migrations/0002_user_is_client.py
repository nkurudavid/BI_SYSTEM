# Generated by Django 4.2.3 on 2023-08-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_client',
            field=models.BooleanField(default=False, verbose_name='Is Client'),
        ),
    ]
