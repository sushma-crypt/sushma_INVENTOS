# Generated by Django 3.2.5 on 2021-08-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0011_rename_tax_add_database_new_taxadd_database_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='productadd_database_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_1', models.CharField(max_length=100)),
                ('item_2', models.CharField(max_length=100)),
                ('item_3', models.CharField(max_length=100)),
                ('item_4', models.CharField(max_length=100)),
                ('item_5', models.CharField(max_length=100)),
                ('item_6', models.CharField(max_length=100)),
                ('item_7', models.CharField(max_length=100)),
                ('item_8', models.CharField(max_length=100)),
                ('item_9', models.CharField(max_length=100)),
            ],
        ),
    ]