# Generated by Django 3.0.4 on 2020-04-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200405_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='checkout_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='magazine',
            name='checkout_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
