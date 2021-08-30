# Generated by Django 3.2.5 on 2021-08-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0005_alter_contact_reg_email_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='usermanagement_add_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=254)),
                ('user_management_add_file', models.FileField(null=True, upload_to='documents')),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
                ('selectstate1', models.CharField(max_length=100)),
                ('selectstate2', models.CharField(max_length=100)),
            ],
        ),
    ]
