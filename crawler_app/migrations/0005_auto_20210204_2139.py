# Generated by Django 3.1.5 on 2021-02-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_app', '0004_auto_20210204_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pchstock',
            name='sell_price',
            field=models.IntegerField(null=True),
        )
    ]
