# Generated by Django 4.2.5 on 2023-12-06 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0006_alter_totalcoinmodel_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bybitmodel',
            table='bybit',
        ),
        migrations.AlterModelTable(
            name='garantexmodel',
            table='garantex',
        ),
        migrations.AlterModelTable(
            name='gateiomodel',
            table='gateio',
        ),
        migrations.AlterModelTable(
            name='hodlhodlmodel',
            table='hodlhodl',
        ),
        migrations.AlterModelTable(
            name='huobimodel',
            table='huobi',
        ),
    ]
