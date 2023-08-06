# Generated by Django 4.1.4 on 2023-08-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=19, verbose_name='Баланс'),
        ),
    ]
