# Generated by Django 3.2.5 on 2021-08-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0015_remove_quotations_database_new_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase_database_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination', models.CharField(max_length=100)),
                ('Supplier', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Total_Amount', models.CharField(max_length=100)),
                ('Paid_Amount', models.CharField(max_length=100)),
                ('Due', models.CharField(max_length=100)),
            ],
        ),
    ]
