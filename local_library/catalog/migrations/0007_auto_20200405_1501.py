# Generated by Django 3.0.4 on 2020-04-05 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200405_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='catalog_user',
            new_name='user',
        ),
    ]