# Generated by Django 3.2.5 on 2021-08-15 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0014_quotations_database_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotations_database_new',
            name='product_description',
        ),
    ]
